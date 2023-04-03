#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """
    Creates a Rectangle object with width and height
    that returns area and perimeter
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width                                 # Getter for width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value                                # Setter for width

    @property
    def height(self):
        return self.__height                                # Getter for height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value                               # Setter for height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (self.__width + self.__height) * 2
