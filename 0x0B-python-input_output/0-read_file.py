#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """
    Reads a file to stdout
    """

    with open(filename, encoding='utf-8') as my_file:
        read_data = my_file.read()
        print(read_data, end='')
