from list_maker import AddToList


class Topping:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class ToppingAmount:
    def __init__(self):
        self.amount = None

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount


class TakeAmount(ToppingAmount):
    def __init__(self):
        super().__init__()

    def take_amount(self):
        self.amount -= 1



onion = Topping()
onion.set_name('Лук')

onion_amount = ToppingAmount()
onion_amount.set_amount(5)

jalapeno = Topping()
jalapeno.set_name('Халапеньо')

jalapeno_amount = ToppingAmount()
jalapeno_amount.set_amount(5)

pickles = Topping()
pickles.set_name('Маринованные огурцы')

pickles_amount = ToppingAmount()
pickles_amount.set_amount(5)

cheese = Topping()
cheese.set_name('Сыр')

cheese_amount = ToppingAmount()
cheese_amount.set_amount(5)


def list_making():
    list = AddToList()
    list.set_list()
    list.add_to_list(onion.get_name())
    list.add_to_list(jalapeno.get_name())
    list.add_to_list(pickles.get_name())
    list.add_to_list(cheese.get_name())
    return list.get_list()