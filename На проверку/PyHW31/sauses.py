from list_maker import AddToList


class Sause:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


ketchup = Sause()
ketchup.set_name('Кетчуп')

mayonaise = Sause()
mayonaise.set_name('Майонез')

mustard = Sause()
mustard.set_name('Горчица')

salsa = Sause()
salsa.set_name('Сальса')


def list_making():
    list = AddToList()
    list.set_list()
    list.add_to_list(ketchup.get_name())
    list.add_to_list(mayonaise.get_name())
    list.add_to_list(mustard.get_name())
    list.add_to_list(salsa.get_name())