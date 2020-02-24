# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen, ziegenhagen@gmail.com
"""

class Classification:
    """
        Classification Item
    """

    def __init__(self):
        self.__label = None
        self.__description = None

    def clear(self):
        self.__label = None
        self.__description = None

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
