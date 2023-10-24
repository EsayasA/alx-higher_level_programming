#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    range_list = []
    for j in range(list_length):
        try:
            division = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            range_list.append(division)
    return range_list
