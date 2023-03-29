#!/usr/bin/python3
"""Square class"""


class Square:
    """Creates square class"""

    def __init__(self, size=0):
        """Initializes square object
        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Getter and Setter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
