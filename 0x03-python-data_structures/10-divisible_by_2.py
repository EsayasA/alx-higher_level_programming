#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    products = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            products.append(True)
        else:
            products.append(False)

    return (products)

