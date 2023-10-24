#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    _list = []
    for j in range(list_length):
        try:
            divide = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            _list.append(divide)
    return _list
