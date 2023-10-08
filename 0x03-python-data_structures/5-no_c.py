#!/usr/bin/python3


def no_c(my_string):
    dup = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(dup))

