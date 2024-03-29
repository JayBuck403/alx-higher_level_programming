#!/usr/bin/python3
"""Base Class"""
import json


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

    def to_json_string(list_dictionaries):
        """Returns a JSON string representation
        of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)


    def save_to_file(cls, list_objs):
        """Write JSON string to file"""
        filename = cls.__name__ + '.json'
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))
