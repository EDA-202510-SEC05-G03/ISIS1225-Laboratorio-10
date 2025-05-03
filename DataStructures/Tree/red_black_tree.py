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
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

from DataStructures.Utils import config
from DataStructures.Tree import rbt_node as node
from DataStructures.Utils import error as error
from DataStructures.List import list as lt
assert config


"""
Implementación de una tabla de simbolos ordenada, mediante un arbol binario
balanceado Red-Black.

Este código está basados en la implementación
propuesta por R.Sedgewick y Kevin Wayne en su libro
Algorithms, 4th Edition
"""

# ________________________________________________________________________
#                     API  RBT
# ________________________________________________________________________

def get_cmpfunction(rbt):
    return rbt.get("cmpfunction", defaultfunction)

def new_map(omaptype="RBT", cmpfunction=None, datastructure="SINGLE_LINKED"):

    """
    Crea una tabla de simbolos ordenada.
    Args:
        compfunction: La funcion de comparacion
    Returns:
        La tabla de símbolos ordenada sin elementos
    Raises:
        Exception
    """
    try:
        rbt = {'root': None,
               'cmpfunction': None,
               'type': omaptype,
               'datastructure': datastructure}

        if(cmpfunction is None):
            rbt['cmpfunction'] = defaultfunction
        else:
            rbt['cmpfunction'] = cmpfunction

        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBT:NewMap')


def put(rbt, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        map: La tabla de simbolos ordenada
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
    Returns:
        La tabla de simbolos
    Raises:
        Exception
    """
    try:
        rbt['root'] = insert_node(rbt['root'], key, value, get_cmpfunction(rbt))
        rbt['root']['color'] = node.BLACK
        return rbt
    except Exception as exp:
        error.reraise(exp, 'Bst:Put')


def get(rbt, key):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.

    Args:
        rbt: El arbol de búsqueda
        key: La llave asociada a la pareja
    Returns:
        La pareja llave-valor en caso de que haya sido encontrada
    Raises:
        Exception
    """
    try:
        return get_node(rbt['root'], key, get_cmpfunction(rbt))

    except Exception as exp:
        error.reraise(exp, 'RBR:get')


def remove(rbt, key):
    try:
        root = rbt['root']
        if root is not None:
            if (not is_red(root['left'])) and (not is_red(root['right'])):
                root['color'] = node.RED
            rbt['root'] = remove_key(root, key, get_cmpfunction(rbt))
            if not is_empty(rbt):
                rbt['root']['color'] = node.BLACK
        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBR:remove')




def contains(rbt, key):
    """
    Retorna True si la llave key se encuentra en la tabla
    o False en caso contrario.
    Es necesario proveer la función de comparación entre llaves.

    Args:
        rbt: El arbol de búsqueda
        key: La llave a buscar
    Returns:
        True si la llave se encuentra en la tabla
    Raises:
        Exception
    """
    try:
        if (rbt['root'] is None):
            return False
        else:
            return (get(rbt, key) is not None)
    except Exception as exp:
        error.reraise(exp, 'RBT: contains')


def size(rbt):
    """
    Retorna el número de entradas en la tabla de simbolos
    Args:
        rbt: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    try:
        return size_tree(rbt['root'])
    except Exception as exp:
        error.reraise(exp, 'Bst:size')


def is_empty(rbt):
    """
    Informa si la tabla de simbolos se encuentra vacia
    Args:
        bst: El arbol de búsqueda
    Returns:
        True si la tabla es vacía, False en caso contrario
    Raises:
        Exception
    """
    try:
        return (rbt['root'] is None)
    except Exception as exp:
        error.reraise(exp, 'Bst:isempty')


def key_set(rbt):
    """
    Retorna una lista con todas las llaves de la tabla
    Args:
        rbt: La tabla de simbolos
    Returns:
        Una lista con todas las llaves de la tabla
    Raises:
        Exception
    """
    try:
        cmpf = get_cmpfunction(rbt)
        klist = lt.new_list(rbt.get('datastructure', 'SINGLE_LINKED'))
        klist = key_set_tree(rbt['root'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'RBT:KeySet')



def value_set(rbt):
    """
    Construye una lista con los valores de la tabla
    Args:
        rbt: La tabla con los elementos
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    try:
        cmpf = get_cmpfunction(rbt)
        vlist = lt.new_list(rbt.get('datastructure', 'SINGLE_LINKED'))
        vlist = value_set_tree(rbt['root'], vlist)
        return vlist
    except Exception as exp:
        error.reraise(exp, 'RBT:valueSet')



def get_min(rbt):
    """
    Retorna el nodo con la menor llave de la tabla de símbolos.
    """
    try:
        if is_empty(rbt):
            return None
        return min_key_tree(rbt['root'])['key']
    except Exception as exp:
        error.reraise(exp, 'RBT:getMin')



def get_max(rbt):
    """
    Retorna el nodo con la mayor llave de la tabla de símbolos.
    """
    try:
        if is_empty(rbt):
            return None
        return max_key_tree(rbt['root'])['key']
    except Exception as exp:
        error.reraise(exp, 'RBT:getMax')



def delete_min(rbt):
    """
    Encuentra y remueve la menor  llave de la tabla de simbolos
    y su valor asociado

    TODO: No implementada en esta versión

    rbt: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        root = rbt['root']
        if (root is not None):
            if ((not is_red(root['left'])) and ((not is_red(root['right'])))):
                root['color'] = node.RED
            root = delete_min_tree(root)
            if (root is not None):
                root['color'] = node.BLACK
        rbt['root'] = root
        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMin')


def delete_max(rbt):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado

    TODO: No implementada en esta versión

    Args:
        rbt: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Exception
    """
    try:
        root = rbt['root']
        if (root is not None):
            if ((not is_red(root['left'])) and ((not is_red(root['right'])))):
                root['color'] = node.RED
            root = delete_max_tree(root)
            if (root is not None):
                root['color'] = node.BLACK
        rbt['root'] = root
        return rbt
    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMin')


def floor(rbt, key):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o
    igual a la llave key

    Args:
        rbt: El arbol de búsqueda
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
    """
    try:
        node = floor_key(rbt['root'], key, get_cmpfunction(rbt))
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'RBT:floor')


def ceiling(rbt, key):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        bst: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    try:
        node = ceiling_key(rbt['root'], key, get_cmpfunction(rbt))
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'RBT:ceiling')


def select(rbt, pos):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        rbt: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    try:
        node = select_key(rbt['root'], pos)
        if (node is not None):
            return node['key']
        return node
    except Exception as exp:
        error.reraise(exp, 'BST:Select')


def rank(rbt, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        rbt: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        El nuemero de llaves encontradas
    Raises:
        Exception
    """
    try:
        return rank_keys(rbt['root'], key, get_cmpfunction(rbt))
    except Exception as exp:
        error.reraise(exp, 'BST:rank')


def height(rbt):
    """
    Retorna la altura del arbol

    Args:
        rbt: El arbol con las parejas
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    try:
        return height_tree(rbt['root'])
    except Exception as exp:
        error.reraise(exp, 'RBT:height')


def keys(rbt, keylo, keyhi):
    cmpf = get_cmpfunction(rbt)
    lstkeys = lt.new_list('SINGLE_LINKED', cmpf)
    return keys_range(rbt['root'], keylo, keyhi, lstkeys, cmpf)

def values(rbt, keylo, keyhi):
    cmpf = get_cmpfunction(rbt)
    lstvalues = lt.new_list('SINGLE_LINKED', cmpf)
    return values_range(rbt['root'], keylo, keyhi, lstvalues, cmpf)



# _____________________________________________________________________________
#       Funciones Helper
# _____________________________________________________________________________


def value_set_tree(root, klist):
    """
    Construye una lista con los valorers de la tabla
    Args:
        root: El arbol con los elementos
        klist: La lista de respuesta
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    try:
        if (root is not None):
            value_set_tree(root['left'], klist)
            lt.add_last(klist, root['value'])
            value_set_tree(root['right'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'RBT:valueSetTree')


def key_set_tree(root, klist):
    """
    Construye una lista con las llaves de la tabla
    Args:
        root: El arbol con los elementos
        klist: La lista de respuesta
    Returns:
        Una lista con todos las llaves
    Raises:
        Exception
    """
    try:
        if (root is not None):
            key_set_tree(root['left'], klist)
            lt.add_last(klist, root['key'])
            key_set_tree(root['right'], klist)
        return klist
    except Exception as exp:
        error.reraise(exp, 'BST:keySetTree')


def rotate_left(rbt):
    """
    rotación izquierda para compensar dos enlaces rojos consecutivos
    """
    try:
        x = rbt['right']
        rbt['right'] = x['left']
        x['left'] = rbt
        x['color'] = x['left']['color']
        x['left']['color'] = node.RED
        x['size'] = rbt['size']
        rbt['size'] = size_tree(rbt['left']) + size_tree(rbt['right']) + 1
        return x
    except Exception as exp:
        error.reraise(exp, 'RBT:rotateLeft')


def rotate_right(rbt):
    """
    Rotación a la derecha para compensar un hijo rojo a la derecha
    Args:
        rbt: El arbol a rotar
    Returns:
        El arbol rotado
    Raises:
        Exception
    """
    try:
        x = rbt['left']
        rbt['left'] = x['right']
        x['right'] = rbt
        x['color'] = x['right']['color']
        x['right']['color'] = node.RED
        x['size'] = rbt['size']
        rbt['size'] = size_tree(rbt['left']) + size_tree(rbt['right']) + 1
        return x
    except Exception as exp:
        error.reraise(exp, 'RBT:rotateRight')


def flip_node_color(rbnode):
    """
    Cambia el color de un nodo
    Args:
        rbnode: El nodo a cambiar
    Returns:
        El nodo con el color opuesto
    Raises:
        Exception
    """
    try:
        if (rbnode is not None):
            if (rbnode['color'] == node.RED):
                rbnode['color'] = node.BLACK
            else:
                rbnode['color'] = node.RED
    except Exception as exp:
        error.reraise(exp, 'RBT:flipNodeColors')


def flip_colors(rbnode):
    """
    Cambia el color de un nodo y de sus dos hijos
    Args:
        maptype: El tipo de map ordenado a utilizar
                 'BST' o 'RBT'
    Returns:
       La tabla de símbolos ordenada sin elementos
    Raises:
        Exception
    """
    try:
        flip_node_color(rbnode)
        flip_node_color(rbnode['left'])
        flip_node_color(rbnode['right'])
    except Exception as exp:
        error.reraise(exp, 'RBT:flipColors')


def is_red(rbnode):
    """
    Indica si un nodo del arbol es rojo
    Args:
       rbnode:  El nodo a examinar
    Returns:
       True / False
    Raises:
        Exception
    """
    try:
        if (rbnode is None):
            return False
        else:
            return (rbnode['color'] == node.RED)
    except Exception as exp:
        error.reraise(exp, 'RBT:isRed')


def size_tree(root):
    """
    Retorna el número de entradas en la a partir un punto dado
    Args:
        root: El arbol de búsqueda
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    try:
        if (root is None):
            return 0
        else:
            return root['size']
    except Exception as exp:
        error.reraise(exp, 'RBT:sizeTree')


def insert_node(root, key, value, cmpfunction):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        root: La raiz del arbol
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
        cmpfunction : Función de comparación
    Returns:
        El arbol con la nueva pareja
    Raises:
        Exception
    """
    try:
        if root is None:     # Se trata de la raíz del árbol
            root = node.new_node(key, value)
            root["color"] = node.RED
            root["size"] = 1

            return root

        cmp = cmpfunction(key, root['key'])

        if (cmp < 0):     # La llave a insertar es menor que la raiz
            root['left'] = insert_node(root['left'],  key, value,
                                      cmpfunction)
        elif (cmp > 0):    # La llave a insertar es mayor que la raíz
            root['right'] = insert_node(root['right'], key, value,
                                       cmpfunction)
        else:              # La llave ya se encuentra en la tabla
            root['value'] = value

        # Se ajusta el balanceo del arbol

        if (is_red(root['right']) and not (is_red(root['left']))):
            root = rotate_left(root)
        if (is_red(root['left']) and is_red(root['left']['left'])):
            root = rotate_right(root)
        if (is_red(root['left']) and is_red(root['right'])):
            flip_colors(root)
        root['size'] = size_tree(root['left']) + size_tree(root['right']) + 1

        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:insertNode')


def height_tree(root):
    """
    Retorna la altura del arbol

    Args:
        root: El arbol con las parejas
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    try:
        if (root is None):
            return -1
        else:
            return 1 + max(height_tree(root['left']), height_tree(root['right']))
    except Exception as exp:
        error.reraise(exp, 'RBT:heightTree')


def get_node(root, key, cmpfunction):
    """
    Retorna la pareja llave, valor, cuya llave sea igual a key.
    Es necesario proveer una función de comparación para las llaves.

    Args:
        root: El arbol rojo-negro
        key: La llave de busqueda
        cmpfunction: funcion de comparación
    Returns:
        La pareja llave-valor
    Raises:
        Exception
    """
    try:
        element = None
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp < 0):
                element = get_node(root['left'], key, cmpfunction)
            elif (cmp > 0):
                element = get_node(root['right'], key, cmpfunction)
            else:
                element = root
        return element

    except Exception as exp:
        error.reraise(exp, 'RBT:getNode')


def min_key_tree(root):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        root: La raiz del arbol de busqueda
    Returns:
        El elemento mas izquierdo del arbol
    Raises:
        Exception
    """
    try:
        min = None
        if (root is not None):
            if (root['left'] is None):
                min = root
            else:
                min = min_key_tree(root['left'])
        return min
    except Exception as exp:
        error.reraise(exp, 'BST:minKeyNode')


def max_key_tree(root):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        bst: La tabla de simbolos
    Returns:
        El elemento mas derecho del árbol
    Raises:
        Exception
    """
    try:
        max = None
        if (root is not None):
            if (root['right'] is None):
                max = root
            else:
                max = max_key_tree(root['right'])
        return max
    except Exception as exp:
        error.reraise(exp, 'BST:maxKeyNode')


def floor_key(root, key, cmpfunction):
    """
    Retorna la llave mas grande en la tabla de simbolos, menor o
    igual a la llave key

    Args:
        rbt: El arbol de búsqueda
        key: La llave
        cmpfunction: Funcion de comparacion
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
    """
    try:
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp == 0):
                return root
            if (cmp < 0):
                return floor_key(root['left'], key, cmpfunction)
            t = floor_key(root['right'], key, cmpfunction)
            if (t is not None):
                return t
            else:
                return root
        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:floorKey')


def ceiling_key(root, key, cmpfunction):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key

    Args:
        rbt: El arbol de búsqueda
        key: La llave
        cmpfunction: Funcion de comparacion
    Returns:
        Retorna la mayor llave de la tabla
    Raises:
        Exception
    """
    try:
        if (root is not None):
            cmp = cmpfunction(key, root['key'])
            if (cmp == 0):
                return root
            if (cmp < 0):
                t = ceiling_key(root['left'], key, cmpfunction)
                if (t is not None):
                    return t
                else:
                    return root
            return ceiling_key(root['right'], key, cmpfunction)
        return None
    except Exception as exp:
        error.reraise(exp, 'BST:ceilingKey')


def rank_keys(root, key, cmpfunction):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        rbt: La tabla de simbolos
        key: La llave de busqueda
    Returns:
       El numero de llaves
    Raises:
        Exception
    """
    try:
        if (root is None):
            return 0
        cmp = cmpfunction(key, root['key'])
        if (cmp < 0):
            return rank_keys(root['left'], key, cmpfunction)
        elif (cmp > 0):
            lsize = size_tree(root['left'])
            rank = rank_keys(root['right'], key, cmpfunction)
            return 1 + lsize + rank
        else:
            return size_tree(root['left'])
    except Exception as exp:
        error.reraise(exp, 'RBT:ranKeys')


def keys_range(root, keylo, keyhi, lstkeys, cmpfunction):
    """
    Retorna todas las llaves del arbol en un rango dado
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    try:
        if (root is not None):
            complo = cmpfunction(keylo, root['key'])
            comphi = cmpfunction(keyhi, root['key'])

            if (complo < 0):
                keys_range(root['left'], keylo, keyhi, lstkeys, cmpfunction)
            if ((complo <= 0) and (comphi >= 0)):
                lt.add_last(lstkeys, root['key'])
            if (comphi > 0):
                keys_range(root['right'], keylo, keyhi, lstkeys, cmpfunction)
        return lstkeys
    except Exception as exp:
        error.reraise(exp, 'RBT:keysRange')


def values_range(root, keylo, keyhi, lstvalues, cmpfunction):
    """
    Retorna todas los valores del arbol en un rango dado por
    [keylo, keyhi]
    Args:
        bst: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superior
    Returns:
        Las llaves en el rango especificado
    Raises:
        Excep
    """
    try:
        if (root is not None):
            complo = cmpfunction(keylo, root['key'])
            comphi = cmpfunction(keyhi, root['key'])

            if (complo < 0):
                values_range(root['left'], keylo, keyhi, lstvalues,
                            cmpfunction)
            if ((complo <= 0) and (comphi >= 0)):
                lt.add_last(lstvalues, root['value'])
            if (comphi > 0):
                values_range(root['right'], keylo, keyhi, lstvalues,
                            cmpfunction)
        return lstvalues
    except Exception as exp:
        error.reraise(exp, 'BST:valuesrange')


def select_key(root, key):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        root: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    try:
        if (root is not None):
            cont = size_tree(root['left'])
            if (cont > key):
                return select_key(root['left'], key)
            elif (cont < key):
                return select_key(root['right'], key-cont-1)
            else:
                return root
        return root
    except Exception as exp:
        error.reraise(exp, 'BST:selectKey')


def delete_min_tree(root):
    """
    Encuentra y remueve la menor  llave de la tabla de simbolos
    y su valor asociado

    root: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        if (root['left'] is None):
            return None
        if ((not is_red(root['left'])) and ((not is_red(root['left']['left'])))):
            root = move_red_left(root)
        root['left'] = delete_min_tree(root['left'])
        root = balance(root)
        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMinTree')


def delete_max_tree(root):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado

    root: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    try:
        if (is_red(root['left'])):
            root = rotate_right(root)

        if (root['right'] is None):
            return None

        if ((not is_red(root['right'])) and
           ((not is_red(root['right']['left'])))):

            root = move_red_right(root)

        root['right'] = delete_max_tree(root['right'])
        root = balance(root)
        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:deleteMinTree')


def move_red_right(root):
    """
    Cambio de color durante el proceso de eliminacion
    root: La tabla de simbolos
    Returns:
        El arbol con un hijo iquierdo de root en negro
    Raises:
        Exception
    """
    try:
        flip_colors(root)
        if (is_red(root['left']['left'])):
            root = rotate_right(root)
            flip_colors(root)
        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:moveRedLeft')


def move_red_left(root):
    """
    Cambio de color durante el proceso de eliminacion
    root: La tabla de simbolos
    Returns:
        El arbol con un hijo iquierdo de root en negro
    Raises:
        Exception
    """
    try:
        flip_colors(root)
        if (is_red(root['right']['left'])):
            root['right'] = rotate_right(root['right'])
            root = rotate_left(root)
            flip_colors(root)
        return root
    except Exception as exp:
        error.reraise(exp, 'RBT:moveRedLeft')


def balance(root):
    """
    Balancea el arbol
    root: Raiz del arbol a balancear
    Returns:
        El arbol balanceado
    Raises:
        Exception
    """
    try:
        if (is_red(root['right'])):
            root = rotate_left(root)

        if (is_red(root['left']) and is_red(root['left']['left'])):
            root = rotate_right(root)

        if (is_red(root['left']) and is_red(root['right'])):
            flip_node_color(root)

        lsize = size_tree(root['left'])
        rsize = size_tree(root['right'])
        root['size'] = 1 + lsize + rsize

        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:moveRedLeft')


def remove_key(root, key, cmpfunction):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        root: El arbol de búsqueda
        key: La llave asociada a la pareja
        cmpfunction : La funcion de comparacion
    Returns:
        El arbol sin la pareja key-value
    Raises:
        Exception
    """
    try:
        if (cmpfunction(key, root['key']) < 0):
            if ((not is_red(root['left'])) and
               (not is_red(root['left']['left']))):
                root = move_red_left(root)
            root['left'] = remove_key(root['left'], key, cmpfunction)
        else:
            if (is_red(root['left'])):
                root = rotate_right(root)

            if ((cmpfunction(key, root['key']) == 0) and
               (root['right'] is None)):
                return None

            if ((not is_red(root['right']) and
               (not is_red(root['right']['left'])))):
                root = move_red_right(root)

            if ((cmpfunction(key, root['key']) == 0)):
                temp = min_key_tree(root['right'])
                root['key'] = temp['key']
                root['value'] = temp['value']
                root['right'] = delete_min_tree(root['right'])
            else:
                root['right'] = remove_key(root['right'], key, cmpfunction)
        root = balance(root)
        return root

    except Exception as exp:
        error.reraise(exp, 'RBT:removeKey')


def defaultfunction(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1