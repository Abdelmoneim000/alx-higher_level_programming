#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > len(tuple_b):
        new_t = list(tuple_a)
    else:
        new_t = list(tuple_b)
    if len(tuple_a) > len(tuple_b):
        for i in range(len(new_t)):
            if len(tuple_b) - 1 < i:
                new_t[i] = new_t[i] + 0
            else:
                new_t[i] = new_t[i] + tuple_b[i]
    else:
        for i in range(len(new_t)):
            if len(tuple_a) - 1 < i:
                new_t[i] = new_t[i] + 0
            else:
                new_t[i] = new_t[i] + tuple_a[i]
    return tuple(new_t)
