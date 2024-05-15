from list_maker import AddToList


class RecipeName:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


standart = RecipeName()
standart.set_name('Стандартный')

mexican = RecipeName()
mexican.set_name('Мексиканский')

vegan = RecipeName()
vegan.set_name('Веганский')


def list_making():
    list = AddToList()
    list.set_list()
    list.add_to_list(standart.get_name())
    list.add_to_list(mexican.get_name())
    list.add_to_list(vegan.get_name())
