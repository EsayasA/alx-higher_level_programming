#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    products = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            products.append(True)
        else:
            products.append(False)

    return (products)
