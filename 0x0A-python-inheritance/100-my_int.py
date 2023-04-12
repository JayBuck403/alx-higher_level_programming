#!/usr/bin/python3
"""MyInt class extends Integer class"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, value):
        """Override == operator"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator"""
        return self.real == value
