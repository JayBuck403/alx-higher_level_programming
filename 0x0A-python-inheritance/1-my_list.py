#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """
    MyList class inherits from built-in
    list class
    """

    def print_sorted(self):
        """
        Prints a list in ascending order
        """
        print(sorted(self))
