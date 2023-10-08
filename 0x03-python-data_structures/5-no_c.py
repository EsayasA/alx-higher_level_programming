#!/usr/bin/python3


def no_c(my_string):
    rep = [y for y in my_string if y != 'c' and y != 'C']
    return ("".join(rep))

