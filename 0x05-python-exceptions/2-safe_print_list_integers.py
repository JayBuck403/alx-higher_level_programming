#!/usr/bin/python3

def safe_print_list_integer(my_list=[], x=0):
    """Print the first x integer elements of a list"""

    total = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i], end="")
            total += 1
        except (ValueError, TypeError):
            continue
    print("")
    return total
