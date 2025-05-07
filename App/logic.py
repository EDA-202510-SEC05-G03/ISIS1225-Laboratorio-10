import csv
import time
import os

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

from DataStructures.Graph import adj_list_graph as gr
from DataStructures.Map import map_linear_probing as m
from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import priority_queue as pq

def init():
    return new_analyzer()

def compare_stops(stop_id1, stop_id2):
    if stop_id1 == stop_id2:
        return 0
    elif stop_id1 > stop_id2:
        return 1
    else:
        return -1

def compare_distances(connection1, connection2):
    if connection1['distance'] == connection2['distance']:
        return 0
    elif connection1['distance'] > connection2['distance']:
        return 1
    else:
        return -1

def new_analyzer():
    analyzer = {
        'stops': m.new_map(1000, 0.7),
        'connections': gr.adj_list_graph(directed=True),
        'components': lt.new_list(),
        'paths': None,
        'priority_queue': pq.new_heap(compare_distances)
    }
    return analyzer
def load_services(analyzer, services_file):
    start_time = get_time()
    
    try:
        services_file = os.path.join(data_dir, services_file)
        
        input_file = csv.DictReader(open(services_file, encoding="utf-8"), delimiter=",")
        
        total_routes = 0
        total_stops = 0
        route_prev_stops = {}
        for service in input_file:
            contador += 1
            service_id = service['ServiceNo']
            direction = service['Direction']
            stop_sequence = int(service['StopSequence'])
            bus_stop_code = service['BusStopCode']
            if service['Distance'] != '':
                distance = float(service['Distance'])
            else:
                distance = 0.0

            route_id = f"{service_id}-{direction}"
            
            stop_info = m.get(analyzer['stops'], bus_stop_code)
            
            
            if stop_info is None:
                stop_info = {
                    'code': bus_stop_code,
                    'routes': lt.new_list()
                    }
                m.put(analyzer['stops'], bus_stop_code, stop_info)
                total_stops += 1
                analyzer['connections'].insert_vertex(bus_stop_code)
            
            route_list = stop_info['routes']
            
            found = False
            i = 0
            while i < lt.size(route_list):
                route = lt.get_element(route_list, i)
                if route is not None and route['id'] == route_id:
                    found = True
                    break
                i += 1
            
            if not found:
                route_info = {
                    'id': route_id,
                    'service': service_id,
                    'direction': direction
                }
                lt.add_last(route_list, route_info)
                total_routes += 1
            
            if stop_sequence > 1:
                prev_stop_code = route_prev_stops.get(route_id)
                
                if prev_stop_code:
                    analyzer['connections'].add_edge(prev_stop_code, bus_stop_code, distance)

                    connection_info = {
                        'distance': distance
                    }

                    pq.insert(analyzer['priority_queue'], connection_info, {
                        'from': prev_stop_code,
                        'to': bus_stop_code,
                        'distance': distance,
                        'route_id': route_id
                    })
            
            route_prev_stops[route_id] = bus_stop_code


        connected = connected_components(analyzer)
        end_time = get_time()
        
        print(f"Tiempo de procesamiento: {delta_time(end_time, start_time)} ms")
        print(f"Total de paradas: {total_stops}")
        print(f"Total de rutas: {total_routes}")
        print(f"Número de componentes conectados: {connected}")
        
        return analyzer

    except Exception as exp:
        print(f"Error en carga de servicios: {exp}")
        import traceback
        traceback.print_exc()
        return None



def connected_components(analyzer):
    visited = {}
    for stop_code in analyzer['connections'].all_vertices():
        visited[stop_code] = False

    cc_count = 0

    for stop_code in analyzer['connections'].all_vertices():
        if not visited[stop_code]:
            cc_count += 1
            component = lt.new_list()
            dfs(analyzer['connections'], stop_code, visited, component)
            lt.add_last(analyzer['components'], component)

    return cc_count

def dfs(graph, start_vertex, visited, component):
  
    stack = []
    stack.append(start_vertex)
    
    while len(stack) > 0:
        vertex = stack.pop()
        
        if not visited.get(vertex, False):
 
            visited[vertex] = True
            lt.add_last(component, vertex)

            for adj_vertex in graph.get_adjacent_vertices(vertex):
                if not visited.get(adj_vertex, False):
                    stack.append(adj_vertex)

def get_time():
    return float(time.perf_counter() * 1000)

def delta_time(end, start):
    return float(end - start)
