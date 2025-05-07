"""
Module to implement a priority queue using a heap-like structure.

This module implements a priority queue that matches the test requirements.
"""

# import python modules
from typing import Any, Callable

# import modules for data structures
from DataStructures.List import arraylist as arlt

# import error handler
from DataStructures.Utils import error


def dflt_heap_elm_cmp(id1: Any, id2: Any) -> int:
    """dflt_heap_elm_cmp is the default comparison function for elements in the array list.

    Args:
        id1 (Any): first element to compare.
        id2 (Any): second element to compare.

    Returns:
        int: returns 1 if id1 > id2, -1 if id1 < id2, 0 if id1 == id2
    """
    if id1 > id2:
        return 1
    elif id1 < id2:
        return -1
    return 0


def new_heap(cmp_function: Callable[[Any, Any], int] = None) -> dict:
    """new_heap creates a new heap for the priority queue.

    Args:
        cmp_function (Callable[[Any, Any], int]): comparison function for elements in the heap.
                                                By default, it is None, in which case the default
                                                comparison function (dflt_heap_elm_cmp) is used.

    Returns:
        dict: dictionary representing the heap with the following fields:
            - elements: list of elements in the heap.
            - size: size of the heap.
            - cmp_function: comparison function for elements in the heap.
    """
    try:
        _heap = {
            "elements": None,
            "size": 0,
            "cmp_function": cmp_function
        }
        if cmp_function is None:
            _heap["cmp_function"] = dflt_heap_elm_cmp

        # Create the elements list
        _heap["elements"] = arlt.new_list(_heap["cmp_function"])
        return _heap
    except Exception as exp:
        error.error_handler("minpq", "new_heap()", exp)


def size(heap: dict) -> int:
    """size returns the number of elements in the heap.

    Args:
        heap (dict): dictionary representing the heap.

    Returns:
        int: size of the heap.
    """
    try:
        return heap["size"]
    except Exception as exp:
        error.error_handler("minpq", "size()", exp)


def is_empty(heap: dict) -> bool:
    """is_empty indicates if the heap is empty.

    Args:
        heap (dict): dictionary representing the heap.

    Returns:
        bool: True if the heap is empty, False otherwise.
    """
    try:
        return heap["size"] == 0
    except Exception as exp:
        error.error_handler("minpq", "is_empty()", exp)


def insert(heap: dict, key: Any, value: Any) -> None:
    """insert inserts a new element in the heap.

    Args:
        heap (dict): dictionary representing the heap.
        key (Any): key of the element to insert.
        value (Any): value of the element to insert.
    """
    try:
        # Create entry with key and value
        entry = {
            "key": key,
            "value": value
        }
        # Add entry to the heap
        arlt.add_last(heap["elements"], entry)
        # Update size
        heap["size"] += 1
        # Maintain heap property
        _swim(heap, heap["size"] - 1)
    except Exception as exp:
        error.error_handler("minpq", "insert()", exp)


def get_first_priority(heap: dict) -> Any:
    """get_first_priority returns the key of the first element in the heap (the minimum).

    Args:
        heap (dict): dictionary representing the heap.

    Returns:
        Any: key of the first element in the heap.
    """
    try:
        if heap["size"] == 0:
            return None

        # Get the first element (minimum)
        first_element = arlt.get_element(heap["elements"], 0)
        return first_element["key"]
    except Exception as exp:
        error.reraise(exp, 'minpq:get_first_priority')


def remove(heap: dict) -> Any:
    """remove removes and returns the key of the first element (minimum) in the heap.

    Args:
        heap (dict): dictionary representing the heap.

    Returns:
        Any: key of the first element in the heap.
    """
    try:
        if heap["size"] == 0:
            return None

        # Get the first element (minimum)
        first_element = arlt.get_element(heap["elements"], 0)
        # Get the last element
        last_element = arlt.get_element(heap["elements"], heap["size"] - 1)
        # Replace the first element with the last
        arlt.update(heap["elements"], 0, last_element)
        # Remove the last element
        arlt.update(heap["elements"], heap["size"] - 1, None)
        # Update size
        heap["size"] -= 1
        # Maintain heap property
        _sink(heap, 0)
        # Return the key of the removed element
        return first_element["key"]
    except Exception as exp:
        error.reraise(exp, 'minpq:remove')


def _swim(heap: dict, idx: int) -> None:
    """_swim makes the element at the specified index swim up the heap to maintain the heap property.

    Args:
        heap (dict): dictionary representing the heap.
        idx (int): index of the element to swim up.
    """
    try:
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent = arlt.get_element(heap["elements"], parent_idx)
            element = arlt.get_element(heap["elements"], idx)
            
            # If parent is greater than element, swap them
            if heap["cmp_function"](parent["key"], element["key"]) > 0:
                arlt.exchange(heap["elements"], idx, parent_idx)
                idx = parent_idx
            else:
                break
    except Exception as exp:
        error.error_handler("minpq", "_swim()", exp)


def _sink(heap: dict, idx: int) -> None:
    """_sink makes the element at the specified index sink down the heap to maintain the heap property.

    Args:
        heap (dict): dictionary representing the heap.
        idx (int): index of the element to sink down.
    """
    try:
        while True:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            smallest = idx
            
            # Find the smallest among the node and its children
            if left_idx < heap["size"]:
                left = arlt.get_element(heap["elements"], left_idx)
                current = arlt.get_element(heap["elements"], smallest)
                if heap["cmp_function"](current["key"], left["key"]) > 0:
                    smallest = left_idx
                    
            if right_idx < heap["size"]:
                right = arlt.get_element(heap["elements"], right_idx)
                current = arlt.get_element(heap["elements"], smallest)
                if heap["cmp_function"](current["key"], right["key"]) > 0:
                    smallest = right_idx
                    
            # If the smallest is not the current node, swap them
            if smallest != idx:
                arlt.exchange(heap["elements"], idx, smallest)
                idx = smallest
            else:
                break
    except Exception as exp:
        error.error_handler("minpq", "_sink()", exp)