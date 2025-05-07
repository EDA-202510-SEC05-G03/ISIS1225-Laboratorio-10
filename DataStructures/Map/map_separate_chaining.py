import random
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    table = lt.new_list('ARRAY_LIST')
    for _ in range(capacity):
        lt.add_last(table, sll.new_list())

    map_table = {
        'prime': prime,
        'capacity': capacity,
        'scale': 1,
        'shift': 0,
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    return map_table


def put(my_map, key, value):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], pos)
    found = False

    for i in range(sll.size(bucket)):
        entry = sll.get_element(bucket, i)
        if me.get_key(entry) == key:
            me.set_value(entry, value)
            found = True
            break

    if not found:
        entry = me.new_map_entry(key, value)
        sll.add_last(bucket, entry)
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']

    if my_map['current_factor'] >= my_map['limit_factor']:
        my_map = rehash(my_map)

    return my_map


def contains(my_map, key):
    return get(my_map, key) is not None


def remove(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], pos)

    for i in range(sll.size(bucket)):
        entry = sll.get_element(bucket, i)
        if me.get_key(entry) == key:
            sll.delete_element(bucket, i + 1)
            my_map['size'] -= 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']
            break

    return my_map


def get(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = lt.get_element(my_map['table'], pos)

    for i in range(sll.size(bucket)):
        entry = sll.get_element(bucket, i)
        if me.get_key(entry) == key:
            return me.get_value(entry)
    return None


def size(my_map):
    return my_map['size']


def is_empty(my_map):
    return my_map['size'] == 0


def key_set(my_map):
    keys = lt.new_list('ARRAY_LIST')
    for i in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], i)
        for j in range(sll.size(bucket)):
            entry = sll.get_element(bucket, j)
            lt.add_last(keys, me.get_key(entry))
    return keys


def value_set(my_map):
    values = lt.new_list('ARRAY_LIST')
    for i in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], i)
        for j in range(sll.size(bucket)):
            entry = sll.get_element(bucket, j)
            lt.add_last(values, me.get_value(entry))
    return values


def rehash(my_map):
    new_capacity = mf.next_prime(my_map['capacity'] * 2)

    new_table = lt.new_list('ARRAY_LIST')
    for _ in range(new_capacity):
        lt.add_last(new_table, sll.new_list())

    for i in range(my_map['capacity']):
        bucket = lt.get_element(my_map['table'], i)
        for j in range(sll.size(bucket)):
            entry = sll.get_element(bucket, j)
            key = me.get_key(entry)
            value = me.get_value(entry)
            pos = mf.hash_value({
                'capacity': new_capacity,
                'prime': my_map['prime'],
                'scale': my_map['scale'],
                'shift': my_map['shift']
            }, key)
            new_bucket = lt.get_element(new_table, pos)
            sll.add_last(new_bucket, me.new_map_entry(key, value))

    my_map['table'] = new_table
    my_map['capacity'] = new_capacity
    my_map['current_factor'] = my_map['size'] / my_map['capacity']

    return my_map
