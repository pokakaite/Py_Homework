from abc import abstractmethod


class HotDog:
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add_ingredients(self):
        pass


class StandartHotDog():
    def __init__(self, bun, ketchup, sausage):
        self.name = 'Классический хот-дог'
        self.ingredients = [bun, ketchup, sausage]


    def show(self, price):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: {price}'
        print(st)

    def add_ingredients(self):
        pass

class HandMadeHotDog:
    def __init__(self, bun, sausage):
        self.name = 'Сделай сам хот-дог'
        self.ingredients = [bun, sausage]

    def show(self, price):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: {price}'
        print(st)

    def add_ingredients(self, data):
        self.ingredients.append(data)
