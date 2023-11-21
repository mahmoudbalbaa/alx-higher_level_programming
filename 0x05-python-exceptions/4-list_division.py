#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for x in range(list_length):
        try:
            res = float(my_list_1[x] / my_list_2[x])
            res_list.append(res)
        except ZeroDivisionError:
            print("division by 0")
            res_list.append(0)
        except TypeError:
            print("wrong type")
            res_list.append(0)
        except IndexError:
            print("out of range")
            res_list.append(0)
        finally:
            pass
    return res_list
