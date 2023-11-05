#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            nw_list = my_list.copy()
            nw_list[idx] = element
            return nw_list
