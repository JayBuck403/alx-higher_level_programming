#!/usr/bin/python3
"""Function that converts string to JSON object"""
import json


def from_json_string(my_str):
    """
    Return an object represented by
    a JSON string
    """

    return json.loads(my_str)
