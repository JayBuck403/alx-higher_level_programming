#!/usr/bin/python3
"""Square Class extends Rectangle Class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        """
        Initializes square object
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
