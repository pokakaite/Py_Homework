from list_maker import *


class Bun:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


wheat_bun = Bun()
wheat_bun.set_name('Пшеничная булочка')

rye_bun = Bun()
rye_bun.set_name('Цельнозерновая булочка')

def list_making():
    list = AddToList()
    list.set_list()
    list.add_to_list(wheat_bun.get_name())
    list.add_to_list(rye_bun.get_name())

