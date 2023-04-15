#!/usr/bin/python3
"""Function to create object from JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates Object from JSON file
    """

    with open(filename, 'r') as my_file:
        return json.load(my_file)
