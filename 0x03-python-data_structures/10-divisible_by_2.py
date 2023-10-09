 #!/usr/bin/python3


def divisible_by_2(my_list=[]):
    product = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            product.append(True)
        else:
            product.append(False)

    return (product)
