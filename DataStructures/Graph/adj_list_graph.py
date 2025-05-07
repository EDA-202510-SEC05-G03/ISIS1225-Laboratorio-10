"""
Módulo de implementación de grafos con listas de adyacencia.
Esta implementación se basa en los requerimientos del controlador proporcionado,
que necesita un grafo para representar rutas entre estaciones.
"""
import time

class ListNode:
    """
    Nodo simple para la lista encadenada
    """
    def __init__(self, vertex_id, edge_weight=0):
        """
        Constructor del nodo
        Args:
            vertex_id: identificador del vértice
            edge_weight: peso asociado a la arista
        """
        self.vertex_id = vertex_id
        self.edge_weight = edge_weight
        self.next = None

class EdgeList:
    """
    Lista encadenada para representar las adyacencias de un vértice
    """
    def __init__(self):
        """
        Constructor de la lista de adyacencia
        """
        self.head = None
        self.size = 0

    def add_edge(self, vertex_id, edge_weight=0):
        """
        Agrega una arista a la lista de adyacencia
        Args:
            vertex_id: identificador del vértice destino
            edge_weight: peso de la arista
        """
        new_node = ListNode(vertex_id, edge_weight)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def get_edge(self, vertex_id):
        """
        Busca una arista en la lista de adyacencia
        Args:
            vertex_id: identificador del vértice destino
        Returns:
            El nodo con la arista si existe, None si no existe
        """
        current = self.head
        while current:
            if current.vertex_id == vertex_id:
                return current
            current = current.next
        return None

class Graph:
    """
    Implementación de grafo con listas de adyacencia
    """
    def __init__(self, directed=False):
        """
        Constructor del grafo
        Args:
            directed: indica si el grafo es dirigido (True) o no (False)
        """
        self.vertices = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.directed = directed
        self.indegree = {}  # Diccionario para almacenar el grado de entrada de cada vértice
    
    def insert_vertex(self, vertex_id):
        """
        Inserta un vértice en el grafo
        Args:
            vertex_id: identificador del vértice
        Returns:
            El vértice insertado
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        
        self.vertices[vertex_id] = EdgeList()
        self.num_vertices += 1
        self.indegree[vertex_id] = 0
        return self.vertices[vertex_id]
    
    def add_edge(self, source, destination, weight=0):
        """
        Agrega una arista al grafo
        Args:
            source: vértice origen
            destination: vértice destino
            weight: peso de la arista
        Returns:
            True si se agregó correctamente, False si ya existía
        """
        # Asegurar que existan los vértices
        if source not in self.vertices:
            self.insert_vertex(source)
        if destination not in self.vertices:
            self.insert_vertex(destination)
        
        # Verificar si ya existe la arista
        edge = self.vertices[source].get_edge(destination)
        if edge:
            # Actualizar el peso si la arista ya existe
            edge.edge_weight = weight
            return False
        
        # Agregar la arista
        self.vertices[source].add_edge(destination, weight)
        self.num_edges += 1
        self.indegree[destination] += 1
        
        # Si el grafo no es dirigido, agregar también la arista en sentido contrario
        if not self.directed:
            self.vertices[destination].add_edge(source, weight)
            self.indegree[source] += 1
            # No incrementamos num_edges aquí para no contar las aristas dos veces
        
        return True
    
    def get_adjacent_vertices(self, vertex_id):
        """
        Retorna los vértices adyacentes a un vértice dado
        Args:
            vertex_id: identificador del vértice
        Returns:
            Lista de vértices adyacentes
        """
        if vertex_id not in self.vertices:
            return []
        
        adjacent = []
        current = self.vertices[vertex_id].head
        while current:
            adjacent.append(current.vertex_id)
            current = current.next
        
        return adjacent
    
    def get_edge_weight(self, source, destination):
        """
        Retorna el peso de una arista
        Args:
            source: vértice origen
            destination: vértice destino
        Returns:
            Peso de la arista o None si no existe
        """
        if source not in self.vertices:
            return None
        
        edge = self.vertices[source].get_edge(destination)
        if edge:
            return edge.edge_weight
        return None
    
    def all_vertices(self):
        """
        Retorna todos los vértices del grafo
        Returns:
            Lista de vértices
        """
        return list(self.vertices.keys())
    
    def degree(self, vertex_id):
        """
        Retorna el grado de un vértice
        Args:
            vertex_id: identificador del vértice
        Returns:
            Grado del vértice
        """
        if vertex_id not in self.vertices:
            return 0
        return self.vertices[vertex_id].size

    def indegree_of(self, vertex_id):
        """
        Retorna el grado de entrada de un vértice
        Args:
            vertex_id: identificador del vértice
        Returns:
            Grado de entrada del vértice
        """
        if vertex_id not in self.indegree:
            return 0
        return self.indegree[vertex_id]
    
    def outdegree_of(self, vertex_id):
        """
        Retorna el grado de salida de un vértice
        Args:
            vertex_id: identificador del vértice
        Returns:
            Grado de salida del vértice
        """
        return self.degree(vertex_id)

# Funciones para crear un nuevo grafo
def adj_list_graph(directed=False):
    """
    Crea un nuevo grafo con listas de adyacencia
    Args:
        directed: indica si el grafo es dirigido (True) o no (False)
    Returns:
        Un nuevo grafo
    """
    return Graph(directed)