#!/usr/bin/python3


def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        d = add(a, b)
        for j in range(4, 6):
            j = add(d, j)
        return (d)

    else:
        return(sub(a, b))

