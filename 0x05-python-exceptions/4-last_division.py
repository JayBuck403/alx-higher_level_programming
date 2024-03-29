#!/usr/bin/python3

def last_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element"""

    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(div)
        return new_list
