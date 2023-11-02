#!/usr/bin/python3
"""Module for addition."""


def add_integer(a, b=98):
    """Add two numbers.

    Args:
        a: first element.
        b: second element.

    Raises:
        TypeError: if a, b are not integer or float.

    Returns:
        The sum of the two elements.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
