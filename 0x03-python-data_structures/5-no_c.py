#!/usr/bin/python3

def no_c(my_string):
    return ''.join([character for character in my_string \
            if ord(character) != 99 and ord(character) != 67])
