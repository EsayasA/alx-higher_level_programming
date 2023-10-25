#!/usr/bin/python3
"""Define Square."""


class Square:
    """Represent a function."""

    def __init__(self, size=0):
        """Initialize function square.
        Args:
            size (int): size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area."""
        return (self.__size * self.__size)

