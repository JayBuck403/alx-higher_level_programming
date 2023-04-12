#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """
    Writes text to file
    """

    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
