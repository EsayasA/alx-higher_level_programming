#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dlast = abs(number) % 10
if number < 0:
    dlast = -dlast
    print("Last digit of {} is {} and is".format(number, dlast), end = "")
    if dlast > 5:
        print("and is greater than 5")
    elif dlast == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
