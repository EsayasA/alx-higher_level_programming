#!/usr/bin/python3


def no_c(my_string):
    rep = [z for z in my_string if z != 'c' and z != 'C']
    return ("".join(rep))
