#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        for x in range(2 - len(tuple_a)):
            tuple_a = tuple_a + (0,)
    if len(tuple_b) < 2:
        for x in range(2 - len(tuple_b)):
            tuple_b = tuple_b + (0,)

    res = []
    for i in range(len(tuple_a)):
        res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
