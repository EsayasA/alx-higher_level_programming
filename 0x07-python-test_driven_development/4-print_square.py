#!/usr/bin/python3
"""Module for print_square."""


def print_square(size):
    """Method to print a square with #.

    Args:
        size: The int size of the square's side.

    Raises:
        TypeError: If size is out of int.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
