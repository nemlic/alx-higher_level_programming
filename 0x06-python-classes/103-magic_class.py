#!/usr/bin/python3
# 103-magic_class by Nelson Itaaru
"""writing a python class magicclass"""
import math


class MagicClass:
    """initialise the magic"""

    def __init__(self, radius=0):
        """ handling exceptions """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """return area of magicclass"""
        return self.__radius ** 2 * math.pi

    def circumference(self):

        """return circumference of magicclass"""
        return 2 * math.pi * self.__radius
