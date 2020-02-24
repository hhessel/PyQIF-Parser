# -*- coding: utf-8 -*-
"""
@author: Uwe Ziegenhagen, ziegenhagen@gmail.com
"""

class Category:
    """
        Category Item
    """

    def __init__(self):
        self.clear()

    def clear(self):
        """
            Resets the category
        """
        self.__label = None
        self.__parent = None
        self.__type = None
        self.__description = None

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def description(self):
        return self.__description

    @parent.setter
    def description(self, description):
        self.__description = description

    @property
    def type(self):
        """
            Returns the Type for this category
        """
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type



if __name__ == "__main__":
    """
        Some test code
    """
    c = Category()
    c.label = 'General Expense'
    c.type = "E"
    c.parent = "Expense"
    print(c.label, c.type, c.parent)