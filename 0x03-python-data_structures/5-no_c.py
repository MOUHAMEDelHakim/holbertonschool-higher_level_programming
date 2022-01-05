#!/usr/bin/python3
def no_c(my_string):
    M = ""
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            M += i
    return M
