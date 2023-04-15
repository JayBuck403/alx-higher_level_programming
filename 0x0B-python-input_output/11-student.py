#!/usr/bin/python3
"""Student Class"""


class Student:
    """Creates new Student object"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes Student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get dictionary representation of Student
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
