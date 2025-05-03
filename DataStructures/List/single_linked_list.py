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

def new_list(cmpfunction=None, module='SINGLE_LINKED', key=None, filename=None, delim=','):
    newlist = {
        'first': None,
        'last': None,
        'size': 0,
        'key': key,
        'type': 'SINGLE_LINKED',
        'datastructure': module,
        'elements': list()
    }

    if cmpfunction is None:
        newlist['cmpfunction'] = defaultfunction
    else:
        newlist['cmpfunction'] = cmpfunction

    if filename is not None:
        try:
            input_file = csv.DictReader(open(filename, encoding="utf-8"), delimiter=delim)
            for line in input_file:
                add_last(newlist, line)
        except Exception as e:
            error.reraise(e, 'Error al leer el archivo CSV en new_list: ')
    
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def add_first (my_list, element):
    """ 
    Agrego un elemento al inicio de la single_linked_list
    """
    
    #Creamos un nuevo nodo.
    new_node = {"info": element, "next": my_list["first"]}
    
    #Si la lista es vacia, updateamos ambos el último y el primero
    if my_list["size"] == 0:
        my_list["last"] = new_node
    
    my_list["first"] = new_node
    my_list["size"] += 1
    
    
    
    return my_list
    
    
def add_last(list, element):
    """
    Añade un elemento al final de la lista y actualiza la lista de elementos
    """
    newnode = {'info': element, 'next': None}
    
    if list['first'] is None:
        list['first'] = newnode
        list['last'] = newnode
    else:
        list['last']['next'] = newnode
        list['last'] = newnode

    list['size'] += 1
    
    # Asegurarnos que elements es una lista antes de hacer append
    if not isinstance(list.get('elements'), type([])):
        list['elements'] = []
    list['elements'].append(element)
    
    return list
    
    
def size (my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] > 0:
        return my_list["first"]["info"]
    return None

def get_last_element(my_list):
    if my_list["size"]> 0:
        return my_list["last"]["info"]
    
def is_empty(my_list):
    """
    Retorna True si la lista está vacía
    """
    return my_list["size"] == 0

def last_element(my_list):
    """ Retorna el último elemento de una  lista no vacía.
        No se elimina el elemento.

    Args:
        my_list: La lista a examinar

    Raises:
        Exception
    """
    try:
        if my_list['last'] is not None:
            return my_list['last']['info']
        return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->lastElement: ')
        
def remove_first(my_list):
    """ Remueve el primer elemento de la lista.
    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.  Si la lista
    es vacía se retorna None.
    Args:
        my_list: La lista a examinar

    Raises:
        Exception
    """
    try:
        if my_list['first'] is not None:
            temp = my_list['first']['next']
            node = my_list['first']
            my_list['first'] = temp
            my_list['size'] -= 1
            if (my_list['size'] == 0):
                my_list['last'] = my_list['first']
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->removeFirst: ')
        
        
def new_single_node(element):
    """
    Estructura que contiene la información a guardar en una lista encadenada
    """
    node = {'info': element, 'next': None}
    return(node)

def insert_element(my_list, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.  Se incrementa en 1 el tamaño de la lista.

    Args:
        my_list: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(my_list)

    Raises:
        Exception
    """
    try:
        new_node = new_single_node(element)
        if (my_list['size'] == 0):
            my_list['first'] = new_node
            my_list['last'] = new_node

        elif ((my_list['size'] > 0) and (pos == 1)):
            new_node['next'] = my_list['first']
            my_list['first'] = new_node

        else:
            cont = 1
            prev = my_list['first']
            current = my_list['first']
            while cont < pos:
                prev = current
                current = current['next']
                cont += 1
            new_node['next'] = current
            prev['next'] = new_node

        my_list['size'] += 1
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->insertElement: ')
        
def remove_last(my_list):
    """ Remueve el último elemento de la lista.

    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        my_list: La lista a examinar

    Raises:
        Exception
    """
    try:
        if my_list['size'] > 0:
            if my_list['first'] == my_list['last']:
                node = my_list['first']
                my_list['last'] = None
                my_list['first'] = None
            else:
                temp = my_list['first']
                while temp['next'] != my_list['last']:
                    temp = temp['next']
                node = my_list['last']
                my_list['last'] = temp
                my_list['last']['next'] = None
            my_list['size'] -= 1
            return node['info']
        else:
            return None
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->remoLast: ')
        
def delete_element(my_list, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor o igual al tamaño de la lista.
    Se decrementa en un uno el tamaño de la lista.
    La lista no puede estar vacía.

    Args:
        my_list: La lista a retornar
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        node = my_list['first']
        prev = my_list['first']
        searchpos = 1
        if (pos == 1):
            my_list['first'] = my_list['first']['next']
            my_list['size'] -= 1
        elif(pos > 1):
            while searchpos < pos:
                searchpos += 1
                prev = node
                node = node['next']
            prev['next'] = node['next']
            my_list['size'] -= 1
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->deleteElement: ')

def change_info(my_list, pos, newinfo):
    """ Cambia la información contenida en el nodo de la lista que se encuentra
         en la posición pos.

    Args:
        my_list: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de
        la posición pos

    Raises:
        Exception
    """
    try:
        current = my_list['first']
        cont = 1
        while cont < pos:
            current = current['next']
            cont += 1
        current['info'] = newinfo
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->changeInfo: ')

def exchange(my_list, pos1, pos2):
    """ Intercambia la información en las posiciones pos1 y pos2 de la lista.

    Args:
        my_list: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posición del segundo elemento

    Raises:
        Exception
    """
    try:
        infopos1 = get_element(my_list, pos1)
        infopos2 = get_element(my_list, pos2)
        change_info(my_list, pos1, infopos2)
        change_info(my_list, pos2, infopos1)
        return my_list
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->exchange: ')
        
def sub_list(my_list, pos, numelem):
    """ Retorna una sublista de la lista my_list.

    Se retorna una lista que contiene los elementos a partir de la
    posición pos,con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        my_list: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        sublst = {'first': None,
                  'last': None,
                  'size': 0,
                  }
        cont = 1
        loc = pos
        while cont <= numelem:
            elem = get_element(my_list, loc)
            add_last(sublst, elem)
            loc += 1
            cont += 1
        return sublst
    except Exception as exp:
        error.reraise(exp, 'singlelinkedlist->subList: ')
        
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

def shell_sort(lst, sort_crit):
    n = size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(
                                lst.get_element(lst, j+1),
                                lst.get_element(lst, j-h+1)):
                lst.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst

def shell_sort(lst, sort_crit):
    n = size(lst)  
    h = 1
    while h < n/3:
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and sort_crit(
                                get_element(lst, j),  
                                get_element(lst, j-h)):  
                exchange(lst, j, j-h)  
                j -= h
        h //= 3
    return lst


def insertion_sort(lst, sort_crit):
    if size(lst) <= 1:
        return lst  

    sorted_head = None  
    sorted_tail = None  
    current = lst["first"]  

    while current is not None:
        next_node = current["next"]  

        
        if sorted_head is None or sort_crit(current["info"], sorted_head["info"]):
            
            current["next"] = sorted_head
            sorted_head = current
            if sorted_tail is None:
                sorted_tail = current  
        else:
            
            prev = sorted_head
            while prev["next"] is not None and not sort_crit(current["info"], prev["next"]["info"]):
                prev = prev["next"]

            
            current["next"] = prev["next"]
            prev["next"] = current

            
            if current["next"] is None:
                sorted_tail = current

        current = next_node  

    
    lst["first"] = sorted_head
    lst["last"] = sorted_tail
    return lst