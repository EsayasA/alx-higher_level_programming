#!/usr/bin/python3
"""Define a class."""


class Square:
    """Represent a class of  square."""

    def __init__(self, size=0):
        """Initialize a new function
        Args:
            size (int):length.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
