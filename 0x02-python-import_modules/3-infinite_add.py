#!/usr/bin/python3

import sys
sum1 = 0
for j in range(len(sys.argv) - 1):
    sum1 = sum1 + int(sys.argv[j + 1])
    print("{}".format(sum1))