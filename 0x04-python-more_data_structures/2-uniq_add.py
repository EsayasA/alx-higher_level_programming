#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    n = 0

    for j in unique:
        n += j

    return (n)
