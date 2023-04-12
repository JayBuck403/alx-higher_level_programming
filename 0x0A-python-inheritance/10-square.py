#!/usr/bin/python3
"""Square Class extends BaseGeometry Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        """
        Initializes Square object
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns area of square object
        """

        return self.__size ** 2
