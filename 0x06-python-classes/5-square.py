#!/usr/bin/python3
"""Define function class."""


class Square:
    """Represent a class of square."""

    def __init__(self, size):
        """Initialize function.
        Args:
            size (int): size square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the  character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
