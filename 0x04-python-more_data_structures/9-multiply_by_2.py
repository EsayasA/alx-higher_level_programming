#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    directory = a_dictionary.copy()
    key_list = list(directory.keys())

    for j in key_list:
        directory[j] *= 2

    return (directory)
