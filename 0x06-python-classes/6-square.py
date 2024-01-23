#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor
        Args:
            size: length of a side of the square.
            position (int, int): the position of new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """property for the length of a size of this square
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method"""
        return self.__position

    @property.setter
    def position(self, value):
        """Setter method"""
        if type(value) is tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) is not int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square.
        Returns:
        the size square.
        """
        return self.__size ** 2

    def my_print(self):
        """prints this square"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
