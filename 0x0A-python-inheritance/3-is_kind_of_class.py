#!/usr/bin/python3
"""Function for testing instance"""


def is_kind_of_class(obj, a_class):
    """
    Returns True for object instance,
    otherwise False
    """

    if isinstance(obj, a_class):
        return True
    return False
