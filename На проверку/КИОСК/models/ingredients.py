from abc import abstractmethod

class Ingredients:
    @abstractmethod
    def show(self):
        pass


class BunIngredient(Ingredients):
    def __init__(self):
        self.name = 'Булочка'
        self.price = 10
        self.amount = 1

    def show(self):
        return f'{self.name} - {self.price} - {self.amount} шт.'

    def add(self):
        self.amount += 1


class SausageIngredient(Ingredients):
    def __init__(self):
        self.name = 'Сосиска'
        self.price = 20
        self.amount = 1

    def show(self):
        return f'{self.name} - {self.price} - {self.amount} шт.'

    def add(self):
        self.amount += 1


class KetchupIngredient(Ingredients):
    def __init__(self):
        self.name = 'Кетчуп'
        self.price = 10
        self.amount = 1

    def show(self):
        return f'{self.name} - {self.price} - {self.amount} шт.'

    def add(self):
        self.amount += 1


class MustardIngredient(Ingredients):
    def __init__(self):
        self.name = 'Кетчуп'
        self.price = 10
        self.amount = 1

    def show(self):
        return f'{self.name} - {self.price} - {self.amount} шт.'

    def add(self):
        self.amount += 1


class PickleIngredient(Ingredients):
    def __init__(self):
        self.name = 'Маринованный огурец'
        self.price = 10
        self.amount = 1

    def show(self):
        return f'{self.name} - {self.price} - {self.amount} шт.'

    def add(self):
        self.amount += 1


class OnionIngredient(Ingredients):
    def __init__(self):
        self.name = 'Лук'
        self.price = 10
        self.amount = 1

    def show(self):
        return f'{self.name} - {self.price} - {self.amount} шт.'

    def add(self):
        self.amount += 1
