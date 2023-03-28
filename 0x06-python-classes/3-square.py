#!/usr/bin/python3
"""Square class"""


class Square:
    """Create a new square class"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): size of new square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return (self.__size ** 2)
