class Number:

    def __init__(self):
        self.__number = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def bin(self, item):
        return bin(item)

    def oct(self, item):
        return oct(item)

    def hex(self, item):
        return hex(item)
