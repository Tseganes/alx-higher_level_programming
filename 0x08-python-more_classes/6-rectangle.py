#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a Rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new square.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

        @propety
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @propety
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """Return area"""
            return (self.__width * self.__height)

        def perimeter(self):
            """return perimeter"""
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))

        def __str__(self):
            """Return the printable representation of rectangle.
            Represent th rectangle with the # character.
            """
            if self.__width == 0 or self.__height == 0:
                return ("")

            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width)]
                if i != self.__height - 1:
                    rect.append("\n")
                return ("".join(rect))
            def __repr__(self):
                """Return the string representation of the Rectangle."""
                rect = "Rectangel(" + str(self.__width)
                rect += ", " + str(self.__height) + ")"
                return (rect)
            def __del__(self):
                """print a message for every deletion of  rectangle."""
                type(self).number of instances -= 1
                print("Bye rectangle...")
