#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    maximum = max(list_num)

    for num in list_num:
        if maximum > num:
            sub += num

    return (maximum - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    key_list = list(roman.keys())

    n = 0
    last = 0
    listn = [0]

    for ch in roman_string:
        for r_num in key_list:
            if r_num == ch:
                if roman.get(ch) <= last:
                    n += to_subtract(listn)
                    listn = [roman.get(ch)]
                else:
                    listn.append(roman.get(ch))

                last = roman.get(ch)

    n += to_subtract(listn)

    return (n)
