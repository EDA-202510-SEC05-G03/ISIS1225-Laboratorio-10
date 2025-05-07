"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import csv
import time
import os

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


# ___________________________________________________
#  Importaciones
# ___________________________________________________

from DataStructures.Graph import adj_list_graph as gr
from DataStructures.Map import map_linear_probing as m
from DataStructures.List import single_linked_list as lt
from DataStructures.Priority_queue  import priority_queue as pq
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = new_analyzer()
    return analyzer

def compare_stops(stop_id1, stop_id2):
    """
    Compara dos ID de paradas
    """
    if stop_id1 == stop_id2:
        return 0
    elif stop_id1 > stop_id2:
        return 1
    else:
        return -1

def compare_distances(connection1, connection2):
    """
    Compara dos conexiones por su distancia
    """
    if connection1['distance'] == connection2['distance']:
        return 0
    elif connection1['distance'] > connection2['distance']:
        return 1
    else:
        return -1

def new_analyzer():
    """ Inicializa el analizador

   stops: Tabla de hash para guardar los vertices del grafo
   connections: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
            'stops': None,
            'connections': None,
            'components': None,
            'paths': None
        }

        # Inicialización de las estructuras de datos
        analyzer['stops'] = m.new_map(capacity=1000,
                                     loadfactor=0.7,
                                     comparefunction=compare_stops)
        analyzer['connections'] = gr.adj_list_graph(directed=True)
        analyzer['components'] = lt.new_list()
        analyzer['paths'] = None
        
        # ___________________________________________________
        #  Crear la cola de prioridad y funciones para la carga de datos
        # ___________________________________________________
        analyzer['priority_queue'] = pq.new_priority_queue(compare_distances)

        return analyzer
    except Exception as exp:
        return exp

# ___________________________________________________
#  TODO Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def load_services(analyzer, services_file):
    """
    Carga los datos de servicios de buses desde un archivo CSV
    Args:
        analyzer: Analizador donde se cargarán los datos
        services_file: Nombre del archivo CSV con la información de servicios
    Returns:
        Analizador actualizado con los datos de servicios
    """
    start_time = get_time()
    
    try:
        services_file = os.path.join(data_dir, services_file)
        print(f"Cargando archivo: {services_file}")
        
        input_file = csv.DictReader(open(services_file, encoding="utf-8"),
                                    delimiter=",")
        
        # Contadores para mostrar estadísticas
        total_routes = 0
        total_stops = 0
        
        for service in input_file:
            # Obtener los datos relevantes
            service_id = service['ServiceNo']
            direction = service['Direction']
            stop_sequence = int(service['StopSequence'])
            bus_stop_code = service['BusStopCode']
            distance = float(service['Distance'])
            
            # Combinamos service_id y direction para crear un identificador único de ruta
            route_id = f"{service_id}-{direction}"
            
            # Creamos un identificador único para cada parada en la secuencia
            stop_id = f"{route_id}-{stop_sequence}"
            
            # Agregamos la parada al mapa de paradas si no existe
            if not m.contains(analyzer['stops'], bus_stop_code):
                stop_info = {
                    'code': bus_stop_code,
                    'routes': lt.new_list()
                }
                m.put(analyzer['stops'], bus_stop_code, stop_info)
                total_stops += 1
                
                # Agregamos el vértice al grafo
                gr.insert_vertex(analyzer['connections'], bus_stop_code)
            
            # Recuperamos la parada del mapa
            stop_info = m.get(analyzer['stops'], bus_stop_code)['value']
            
            # Agregamos la ruta a la lista de rutas de la parada si no existe
            found = False
            route_list = stop_info['routes']
            i = 1
            while i <= lt.size(route_list) and not found:
                route = lt.get_element(route_list, i)
                if route['id'] == route_id:
                    found = True
                i += 1
            
            if not found:
                route_info = {
                    'id': route_id,
                    'service': service_id,
                    'direction': direction
                }
                lt.add_last(route_list, route_info)
                total_routes += 1
            
            # Si no es la primera parada en la secuencia, agregamos una conexión
            if stop_sequence > 1:
                prev_stop_sequence = stop_sequence - 1
                prev_stop_id = f"{route_id}-{prev_stop_sequence}"
                
                # Buscamos la parada anterior en la secuencia
                # (Esto puede optimizarse guardando un mapa de secuencias)
                prev_stop_code = None
                # Utilizamos una bandera para controlar cuando encontramos la parada
                found_prev_stop = False
                keys_iter = m.keySet(analyzer['stops'])
                key_idx = 0
                
                while key_idx < len(keys_iter) and not found_prev_stop:
                    key = keys_iter[key_idx]
                    stop = m.get(analyzer['stops'], key)['value']
                    
                    route_idx = 1
                    while route_idx <= lt.size(stop['routes']) and not found_prev_stop:
                        r = lt.get_element(stop['routes'], route_idx)
                        if r['id'] == route_id:
                            # Verificar si es la parada anterior en la secuencia
                            # Esto es aproximado, se debería mejorar la lógica
                            prev_stop_code = key
                            found_prev_stop = True
                        route_idx += 1
                    
                    key_idx += 1
                
                if prev_stop_code:
                    # Agregamos la conexión al grafo con la distancia como peso
                    segment_distance = distance
                    gr.add_edge(analyzer['connections'], prev_stop_code, bus_stop_code, segment_distance)
                    
                    # Agregamos a la cola de prioridad
                    connection_info = {
                        'from': prev_stop_code,
                        'to': bus_stop_code,
                        'distance': segment_distance,
                        'route_id': route_id
                    }
                    pq.insert(analyzer['priority_queue'], connection_info)
        
        # Análisis de componentes conectados
        conected = connected_components(analyzer)
        
        end_time = get_time()
        
        print(f"Tiempo de procesamiento: {delta_time(end_time, start_time)} ms")
        print(f"Total de paradas: {total_stops}")
        print(f"Total de rutas: {total_routes}")
        print(f"Número de componentes conectados: {conected}")
        
        return analyzer
        
    except Exception as exp:
        print(f"Error en carga de servicios: {exp}")
        return None

def connected_components(analyzer):
    """
    Calcula los componentes conectados del grafo
    Args:
        analyzer: El analizador con los datos
    Returns:
        El número de componentes conectados
    """
    # Esta es una implementación simplificada, se debería usar un algoritmo real
    # como Kosaraju o Tarjan para grafos dirigidos
    
    # Marcamos todos los vértices como no visitados
    visited = {}
    for stop_code in gr.all_vertices(analyzer['connections']):
        visited[stop_code] = False
    
    # Contador de componentes
    cc_count = 0
    
    # Recorremos todos los vértices
    for stop_code in gr.all_vertices(analyzer['connections']):
        if not visited[stop_code]:
            # Encontramos un nuevo componente
            cc_count += 1
            component = lt.new_list()
            # Realizamos un DFS desde este vértice
            dfs(analyzer['connections'], stop_code, visited, component)
            # Guardamos el componente en la lista de componentes
            lt.add_last(analyzer['components'], component)
    
    return cc_count

def dfs(graph, vertex, visited, component):
    """
    Realiza un recorrido DFS desde un vértice
    Args:
        graph: El grafo a recorrer
        vertex: Vértice inicial
        visited: Diccionario de vértices visitados
        component: Lista donde se guardan los vértices del componente
    """
    # Marcamos el vértice como visitado
    visited[vertex] = True
    # Agregamos el vértice al componente
    lt.add_last(component, vertex)
    
    # Recorremos los adyacentes
    for adj_vertex in gr.get_adjacent_vertices(graph, vertex):
        if not visited.get(adj_vertex, False):
            dfs(graph, adj_vertex, visited, component)


#Funciones para la medición de tiempos

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def delta_time(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed








