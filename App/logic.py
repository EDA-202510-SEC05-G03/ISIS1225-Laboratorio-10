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

     

        # ___________________________________________________
        #  TODO crear la cola de prioriad y cree las funciones 
        # necesarias para la carga de datos
        # ___________________________________________________

        return analyzer
    except Exception as exp:
        return exp

# ___________________________________________________
#  TODO Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________



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








