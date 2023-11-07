#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return None
        sort_list = sorted(my_list)
        big = sort_list[len(my_list) - 1]

        return big
