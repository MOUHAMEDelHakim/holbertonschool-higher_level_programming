#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        T = my_list[0]
        for i in my_list:
            if i > T:
                T = i
        return T
