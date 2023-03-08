#!/usr/bin/python3

def uppercase(str):
    new_string = ''
    for i in str:
        j = ord(i)
        if j >= 97 and j <= 122:
            new_string += chr(j - 32)
        elif j >= 65 and j <= 90:
            new_string += chr(j)
        else:
            new_string += chr(j)
    print("{}".format(new_string))
