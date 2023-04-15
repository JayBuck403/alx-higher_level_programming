#!/usr/bin/python3
"""Function for inserting text iin a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts text after each line containing a
    given string in a file
    """
    text = ""
    with open(filename) as myfile:
        for line in myfile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as my_file:
        my_file.write(text)
