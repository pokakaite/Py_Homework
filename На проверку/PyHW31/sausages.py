from list_maker import AddToList


class Sausage:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


milky = Sausage()
milky.set_name('Молочная сосиска')

soy = Sausage()
soy.set_name('Соевая сосиска')

chicken = Sausage()
chicken.set_name('Куриная сосиска')


def list_making():
    list_names = AddToList()
    list_names.set_list()
    list_names.add_to_list(milky.get_name())
    list_names.add_to_list(soy.get_name())
    list_names.add_to_list(chicken.get_name())