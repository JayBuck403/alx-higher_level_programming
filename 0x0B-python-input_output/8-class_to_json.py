#!/usr/bin/python3
"""Class to JSON function"""


def class_to_json(obj):
    """
    Returns dictionary description of
    simple data
    """
    return obj.__dict__
