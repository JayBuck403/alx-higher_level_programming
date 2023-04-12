#!/usr/bin/python3
"""Rectangle Class extends BaseGeometry Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        Initializes new rectangle object
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Prints the rectangle description
        """

        to_print = "[" + str(self.__class__.__name__) + "] "
        to_print += str(self.__width) + "/" + str(self.__height)
        return to_print
