#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        rv_list = my_list
        rv_list.reverse()
        for i in range(len(rv_list)):
            print("{:d}".format(rv_list[i]))
