from list_maker import AddToList


class Topping:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


onion = Topping()
onion.set_name('Лук')

jalapeno = Topping()
jalapeno.set_name('Халапеньо')

pickles = Topping()
pickles.set_name('Маринованные огурцы')

cheese = Topping()
cheese.set_name('Сыр')


def list_making():
    list = AddToList()
    list.set_list()
    list.add_to_list(onion.get_name())
    list.add_to_list(jalapeno.get_name())
    list.add_to_list(pickles.get_name())
    list.add_to_list(cheese.get_name())
    return list.get_list()