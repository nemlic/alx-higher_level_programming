#!/usr/bin/python3
# 5-square.py by Nelson Itaaru
"""A module that defines a class square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize a new square class
        Args:
            size: represents the size of the new square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Gets the current  size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns: The area of the square """

        return (self.__size ** 2)

    def my_print(self):
        """print the square in # character """

        if self.__size == 0:
            print("")

        for i in range(self.__size):
            print("#" * self.__size)
