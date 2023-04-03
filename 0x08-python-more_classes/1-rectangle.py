#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self,  width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The size of the new rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif size < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

         Args:
            height (int): The size of the new rectangle.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif size < 0:
            raise ValueError("height must be >= 0")
        self.__size = size
