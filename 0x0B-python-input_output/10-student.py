#!/usr/bin/python3
"""Student Class"""


class Student:
    """
    Creates new Student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes new Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves dictionary representation of
        Student instance
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
