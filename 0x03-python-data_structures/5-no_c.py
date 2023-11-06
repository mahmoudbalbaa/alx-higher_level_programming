#!/usr/bin/python3
def no_c(my_string):
    if isinstance(my_string, str):
        nw_string = list(my_string)
        for i in range(len(nw_string)):
            if nw_string[i] == 'c' or nw_string[i] == 'C':
                nw_string[i] = ''
        return ''.join(nw_string)
