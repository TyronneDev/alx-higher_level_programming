#!/usr/bin/python3
"""
class Square prints a square
"""


class Square:
    """Defines a class Square

    Attributes:
        __size (int): length of side of the square
    """
    def __init__(self, size):
        """Initialization method

        Args:
            size (int): length of side of the square

        Return: None
        """
        self.__size = size
