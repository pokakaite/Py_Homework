from list_maker import AddToList


class Topping:
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class ToppingAmount(Topping):
    def __init__(self):
        super().__init__()
        self.amount = None

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount


class ShowTopping:
    def __init__(self, name, amount, id):
        self.name = name
        self.amount = amount
        self.id = id

    def show_id(self):
        print(f'Топпинг №{self.id}', end=' - ')

    def show_name(self):
        print(self.name)

    def show_amount(self):
        print(f'\tОстаток: {self.amount}.')



onion = ToppingAmount()
onion.set_name('Лук')
onion.set_amount(5)

jalapeno = ToppingAmount()
jalapeno.set_name('Халапеньо')
jalapeno.set_amount(5)

pickles = ToppingAmount()
pickles.set_name('Маринованные огурцы')
pickles.set_amount(5)

cheese = ToppingAmount()
cheese.set_name('Сыр')
cheese.set_amount(5)

show_onion = ShowTopping(onion.get_name(), onion.get_amount(), 1)
show_jalapeno = ShowTopping(jalapeno.get_name(), jalapeno.get_amount(), 2)
show_pickles = ShowTopping(pickles.get_name(), pickles.get_amount(), 3)
show_cheese = ShowTopping(cheese.get_name(), cheese.get_amount(), 4)

