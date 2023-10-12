#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())
    order.sort()
    for j in order:
        print("{}: {}".format(j, a_dictionary.get(j)))
