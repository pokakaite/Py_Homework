from abc import abstractmethod


class Ingredients:
    def __init__(self):
        self.name = None
        self.price = None
        self.amount = None

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')


class BunIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Булочка'
        self.price = 10
        self.amount = 1

    def add(self):
        self.amount += 1


class SausageIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Сосиска'
        self.price = 20
        self.amount = 1

    def add(self):
        self.amount += 1


class VeganSausageIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Соевая сосиска'
        self.price = 40
        self.amount = 1

    def add(self):
        self.amount += 1


class KetchupIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Кетчуп'
        self.price = 10
        self.amount = 1

    def add(self):
        self.amount += 1


class MustardIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Горчица'
        self.price = 10
        self.amount = 1

    def add(self):
        self.amount += 1


class PickleIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Маринованный огурец'
        self.price = 10
        self.amount = 1

    def add(self):
        self.amount += 1


class OnionIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Лук'
        self.price = 10
        self.amount = 1

    def add(self):
        self.amount += 1


class JalapenoIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Халапеньо'
        self.price = 20
        self.amount = 1

    def add(self):
        self.amount += 1


class ShowIngredients(Ingredients):
    def show(self, *items):
        count = 0
        for item in items:
            count += 1
            print(f'{count} - ', end='')
            item.show()
