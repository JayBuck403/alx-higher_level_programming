#!/usr/bin/python3
"""Base Class"""


class Base:
    """
    Creates a Base model for all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
