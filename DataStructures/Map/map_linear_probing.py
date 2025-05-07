import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

__EMPTY__ = me.new_map_entry("__EMPTY__", "__EMPTY__")

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    table = lt.new_list("ARRAY_LIST")
    for _ in range(capacity):
        lt.add_last(table, me.new_map_entry(None, None))
    return {
        'prime': prime,
        'capacity': capacity,
        'scale': 1, 
        'shift': 0,  
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }

def put(my_map, key, value):
    hash_val = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_val)

    if found:
        entry = lt.get_element(my_map['table'], pos)
        me.set_value(entry, value)
        lt.change_info(my_map['table'], pos, entry)
    else:
        new_entry = me.new_map_entry(key, value)
        lt.change_info(my_map['table'], pos, new_entry)
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']

    if my_map['current_factor'] > my_map['limit_factor']:
        my_map = rehash(my_map)

    return my_map

def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    occupied = False
    table = my_map['table']
    while not found:
        if is_available(table, hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = lt.get_element(table, hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, lt.get_element(table, hash_value)) == 0:
            first_avail = hash_value
            found = True
            occupied = True
        hash_value = (hash_value + 1) % my_map["capacity"]
    return occupied, first_avail

def is_available(table, pos):
    entry = lt.get_element(table, pos)
    return me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__"

def default_compare(key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    return -1

def contains(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, _ = find_slot(my_map, key, hash_val)
    return found

def remove(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_val)
    if found:
        lt.change_info(my_map['table'], pos, __EMPTY__)
        my_map['size'] -= 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
    return my_map

def get(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_val)
    if found:
        return me.get_value(lt.get_element(my_map['table'], pos))
    return None

def size(my_map):
    return my_map['size']

def is_empty(my_map):
    return my_map['size'] == 0

def key_set(my_map):
    keys = lt.new_list("ARRAY_LIST")
    for i in range(my_map['capacity']):
        entry = lt.get_element(my_map['table'], i)
        if me.get_key(entry) not in [None, "__EMPTY__"]:
            lt.add_last(keys, me.get_key(entry))
    return keys

def value_set(my_map):
    values = lt.new_list("ARRAY_LIST")
    for i in range(my_map['capacity']):
        entry = lt.get_element(my_map['table'], i)
        if me.get_key(entry) not in [None, "__EMPTY__"]:
            lt.add_last(values, me.get_value(entry))
    return values

def rehash(my_map):
    new_capacity = mf.next_prime(2 * my_map['capacity'])
    new_table = new_map(new_capacity, my_map['limit_factor'], my_map['prime'])
    for i in range(my_map['capacity']):
        entry = lt.get_element(my_map['table'], i)
        if me.get_key(entry) not in [None, "__EMPTY__"]:
            new_table = put(new_table, me.get_key(entry), me.get_value(entry))
    return new_table
