class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

"""to trieve it"""
    def width(self):
        return self.__width
"""to set"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def height(self):
        return self.__height
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
