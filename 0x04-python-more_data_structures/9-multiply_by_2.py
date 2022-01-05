#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    V = {}
    V.update(a_dictionary)
    for i in V:
        V[i] = V[i] * 2
    return V
