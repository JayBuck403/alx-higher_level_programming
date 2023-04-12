#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """
    Appends text to file and creates file if
    file doesn't exist
    """

    with open(filename, 'a+', encoding='utf-8') as my_file:
        return my_file.write(text)
