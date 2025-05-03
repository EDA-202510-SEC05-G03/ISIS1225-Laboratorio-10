import DataStructures.Utils.config as config
from DataStructures.Utils import error as error
from DataStructures.Priority_queue import heap as h
from DataStructures.List import list as lt
assert config


"""
Implementación de una cola de prioridad orientada a menor

Este código está basados en la implementación
propuesta por R.Sedgewick y Kevin Wayne en su libro
Algorithms, 4th Edition
"""


def new_heap(min=True):
    if min:
        cmpfunction = lambda x, y: x < y
    else:
        cmpfunction = lambda x, y: x > y
    try:
        pq = {
            "heap": h.new_heap(cmpfunction),
            "size": 0,
            "elements": lt.new_list(datastructure="ARRAY_LIST", cmpfunction=cmpfunction),  # <- Ahora no es None, es lista vacía
            "cmp_function": cmpfunction
        }
        return pq
    except Exception as exp:
        error.reraise(exp, 'new_heap')



def size(minpq):
    """
    Retorna el número de elementos en la MinPQ
    Args:
        minpq: la cola de prioridad
    Returns:
       El tamaño de la MinPQ
    Raises:
        Exception
    """
    try:
        return (h.size(minpq['heap']))
    except Exception as exp:
        error.reraise(exp, 'minpq:size')


def is_empty(minpq):
    """
    Indica si la MinPQ está vacía
    """
    try:
        return (minpq['size'] == 0)
    except Exception as exp:
        error.reraise(exp, 'minpq:is_empty')



def min(minpq):
    """
    Retorna el primer elemento de la MinPQ, es decir el menor elemento

    Args:
        minpq: La cola de prioridad
    Returns:
      El menor elemento de la MinPQ
    Raises:
        Exception
    """
    try:
        return h.min(minpq['heap'])
    except Exception as exp:
        error.reraise(exp, 'minpq:min')


def insert(minpq, key, value):
    """
    Inserta un nuevo elemento en la cola de prioridad
    """
    try:
        if minpq["elements"] is None:
            minpq["elements"] = lt.new_list(datastructure="ARRAY_LIST", cmpfunction=minpq["cmp_function"])
        
        element = {"key": key, "value": value}
        minpq["heap"] = h.insert(minpq["heap"], element)
        lt.add_last(minpq["elements"], element)
        minpq["size"] += 1
        return minpq
    except Exception as exp:
        error.reraise(exp, 'minpq:insert')





def del_min(minpq):
    """
    Retorna el menor elemento de la MinPQ y lo elimina.
    Se reemplaza con el último elemento y se hace sink.

    Args:
        minpq: La cola de prioridad

    Returns:
        El menor elemento eliminado
    Raises:
        Exception
    """
    try:
        return (h.del_min(minpq['heap']))
    except Exception as exp:
        error.reraise(exp, 'minpq:delMin')
        
def get_first_priority(minpq):
    """
    Retorna la llave del primer elemento en la cola de prioridad (el menor).
    """
    try:
        if minpq['size'] == 0:
            return None
        
        first_element = lt.first_element(minpq["elements"])
        return first_element["key"]
    except Exception as exp:
        error.reraise(exp, 'minpq:get_first_priority')
        
def remove(minpq):
    """
    Elimina y retorna la llave del primer elemento (menor) de la cola de prioridad.
    """
    try:
        if minpq['size'] == 0:
            return None
        
        first_element = lt.remove_first(minpq["elements"])
        minpq['size'] -= 1
        return first_element["key"]
    except Exception as exp:
        error.reraise(exp, 'minpq:remove')





