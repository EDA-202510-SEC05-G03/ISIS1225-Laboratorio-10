"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 * Este programa es software libre bajo la licencia GNU GPL v3.
"""

from DataStructures.Priority_queue import adjlist as gr

"""
Este archivo contiene la implementación del TAD grafo no dirigido.
"""

def new_graph(size=10, cmpfunction=None, directed=False):
    """
    Crea un grafo vacío.

    Args:
        size: Tamaño inicial del grafo
        cmpfunction: Función de comparación
        directed: Indica si el grafo es dirigido o no

    Returns:
        Un nuevo grafo vacío
    """
    return gr.new_graph(size, cmpfunction, directed)


def insertVertex(graph, vertex):
    return gr.insert_vertex(graph, vertex)


def removeVertex(graph, vertex):
    return gr.remove_vertex(graph, vertex)


def numVertices(graph):
    return gr.num_vertices(graph)


def numEdges(graph):
    return gr.num_edges(graph)


def vertices(graph):
    return gr.vertices(graph)


def edges(graph):
    return gr.edges(graph)


def degree(graph, vertex):
    return gr.degree(graph, vertex)


def outdegree(graph, vertex):
    return gr.outdegree(graph, vertex)


def indegree(graph, vertex):
    return gr.indegree(graph, vertex)


def getEdge(graph, vertexa, vertexb):
    return gr.get_edge(graph, vertexa, vertexb)


def addEdge(graph, vertexa, vertexb, weight=0):
    return gr.add_edge(graph, vertexa, vertexb, weight)


def containsVertex(graph, vertex):
    return gr.contains_vertex(graph, vertex)


def adjacents(graph, vertex):
    return gr.adjacents(graph, vertex)


def adjacentEdges(graph, vertex):
    return gr.adjacent_edges(graph, vertex)
