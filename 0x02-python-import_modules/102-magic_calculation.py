#!/usr/bin/python3


def magic_calculation(x, y):
    from magic_calculation_102 import add, sub

    if x < y:
        c = add(x, y)
        for j in range(4, 6):
            d = add(d, j)
        return (d)

    else:
        return(sub(x, y))
