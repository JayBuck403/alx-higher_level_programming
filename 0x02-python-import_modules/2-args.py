#!/usr/bin/python

if __name__ == "__main":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        j = 0
        for arg in sys.argv:
            print("{}: {}".format(i, arg))
            j++
