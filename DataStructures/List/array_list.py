import sys
import os

# Agrega el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from DataStructures.Utils import config
from DataStructures.Utils import error as error
import csv
assert config
from typing import Callable
from typing import Any

def new_list(cmpfunction=None, module=None, key=None, filename=None, delim=None):
    """Crea una lista vacía.

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Un diccionario que representa la estructura de datos de una lista

    Raises:

    """
    newlist = {'elements': [],
               'size': 0,
               'type': 'ARRAY_LIST',
               'cmpfunction': cmpfunction,
               'key': key,
               'datastructure': module
               }

    if(cmpfunction is None):
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if (filename is not None):
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=delim)
        for line in input_file:
            add_last(newlist, line)
    return (newlist)


def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    """
    Agrega un elemento al principio de la lista. 
    Para esto, debemos incrementar tambien el size de la lista.
    """
    #Insert nos ayuda escoger el indice donde lo queremos insertar.
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    """
    Agrega un elemento al final de una lista.
    Debemos seguir incrementando el size de la lista.
    """
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):    
    """
    Devuelve la longitud de la lista
    """
    return my_list["size"]
    
def first_element(my_list):
    """
    Retorna el primer elemento de la lista.
    """
    if my_list["size"]>0:
        primer_elemento = my_list["elements"][0]
    else:
        primer_elemento = None
    return primer_elemento

def last_element(lst):
    """ Retorna el último elemento de una  lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lst['elements'][lst['size']-1]
    except Exception as exp:
        error.reraise(exp, 'arraylist->lastElement: ')
        
def is_empty(my_list):
    """
    Retorna True si la lista está vacía
    """
    return my_list["size"] == 0

def insert_element(my_list, element, pos):
    """
    Inserta un elemento en una posición dada.
    """
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    """
    Elimina un elemento en una posición dada.
    """
    my_list["elements"].pop(pos)
    my_list["size"] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    """"
    Cambia la información de un elemento en una posición dada
    """
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    """
    Intercambia la información de dos elementos en las posiciones dadas.
    """
    info_1 = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = info_1
    return my_list


def remove_first(my_list):
    """
    Elimina el primer elemento de la lista
    """
    elemento_eliminado = my_list["elements"][0]
    my_list["elements"].pop(0)
    my_list["size"] -= 1
    return elemento_eliminado

def remove_last(my_list):
    """
    Elimina el primer elemento de la lista
    """
    elemento_eliminado = my_list["elements"][-1]
    my_list["elements"].pop(-1)
    my_list["size"] -= 1
    return elemento_eliminado

def sub_list(my_list, pos_i, num_elements):
    pos_f = pos_i + num_elements
    elements = my_list["elements"]
    sublist = elements[pos_i:pos_f]
    return {'elements': sublist,'size': len(sublist)}

def update(lt: dict, pos: int, element: Any) -> None:
    """update updates an element in a specific position in the array list.

    Args:
        lt (dict): array list to update the element.
        pos (int): position to update the element.
        element (Any): element to update in the array list.
    """
    try:
        lt["elements"][pos] = element
        # lt.get("elements")[pos] = element
    except Exception as exp:
        error("arraylist", "update()", exp)

def defaultfunction(id1, id2):
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0

def default_sort_criteria(element_1, element_2):
    is_sorted = defaultfunction(element_1,element_2)
    return is_sorted

def merge_sort(lst: dict, sort_crit: Callable) -> dict:
    list_size = size(lst)
    if list_size <= 1:  # Handle empty or single element lists
        return lst
        
    if list_size > 1:
        mid = list_size // 2
        # Create sublists correctly
        _left_lt = sub_list(lst, 0, mid)
        _right_lt = sub_list(lst, mid, list_size - mid)
        
        # Sort sublists
        merge_sort(_left_lt, sort_crit)
        merge_sort(_right_lt, sort_crit)
        
        # Merge process
        i = j = k = 0
        _n_left = size(_left_lt)
        _n_right = size(_right_lt)

        while (i < _n_left) and (j < _n_right):
            elemi = _left_lt["elements"][i]  # Direct access instead of get_element
            elemj = _right_lt["elements"][j]  # Direct access instead of get_element
            if sort_crit(elemj, elemi):
                lst["elements"][k] = elemj
                j += 1
            else:
                lst["elements"][k] = elemi
                i += 1
            k += 1

        while i < _n_left:
            lst["elements"][k] = _left_lt["elements"][i]  # Direct access
            i += 1
            k += 1

        while j < _n_right:
            lst["elements"][k] = _right_lt["elements"][j]  # Direct access
            j += 1
            k += 1
    return lst

    

def selection_sort(lst, sort_criteria: callable) -> dict:
    list_size = size(lst)  # Change variable name to avoid shadowing the function
    pos1 = 0
    while pos1 < list_size:
        minimum = pos1    
        pos2 = pos1 + 1
        while (pos2 < list_size):  # Changed <= to < to avoid index out of range
            if (sort_criteria(get_element(lst, pos2),
               get_element(lst, minimum))):
                minimum = pos2  
            pos2 += 1
        exchange(lst, pos1, minimum)  
        pos1 += 1
    return lst

def partition(lst, lo, hi, sort_crit):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if sort_crit(
           get_element(lst, leader), get_element(lst, hi)):
            exchange(lst, follower, leader)
            follower += 1
        leader += 1
    exchange(lst, follower, hi)
    return follower


def sort(lst, lo, hi, sort_crit):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if lo >= hi:
        return
    pivot = partition(lst, lo, hi, sort_crit)
    sort(lst, lo, pivot-1, sort_crit)  # Changed quick_sort to sort for recursion
    sort(lst, pivot+1, hi, sort_crit)  # Changed quick_sort to sort for recursion


def quick_sort(lst, sort_crit):
    if size(lst) <= 1:  # Handle empty or single element lists
        return lst
    sort(lst, 0, size(lst)-1, sort_crit)  # Changed 1 to 0 for starting index, and size to size-1
    return lst


def insertion_sort(lst, sort_crit):
    n = lst["size"]  
    pos1 = 1  

    while pos1 < n:
        pos2 = pos1
        while pos2 > 0 and sort_crit(lst["elements"][pos2], lst["elements"][pos2 - 1]):  
            lst["elements"][pos2], lst["elements"][pos2 - 1] = lst["elements"][pos2 - 1], lst["elements"][pos2]
            pos2 -= 1
        pos1 += 1  

    return lst

def shell_sort(lst, sort_crit):
    """
    Implementación del algoritmo Shell Sort para ArrayList
    """

    n = lst["size"]
    h = 1
    
    while h < n/3:
        h = 3*h + 1
        

    while h >= 1:
        for i in range(h, n):
            j = i

            while j >= h and sort_crit(
                    lst["elements"][j],       
                    lst["elements"][j-h]):    

                lst = exchange(lst, j, j-h)
                j -= h
        h //= 3  
        
    return lst

