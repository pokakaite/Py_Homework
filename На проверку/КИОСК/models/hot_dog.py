from abc import abstractmethod


# рецепты хот-догов. добавление ингредиентов. вывод информации в консоль


class HotDog:
    def __init__(self):
        self.name = None
        self.ingredients = None

    @abstractmethod
    def show(self, price):
        pass

    @abstractmethod
    def add_ingredients(self):
        pass


class StandartHotDog:
    def __init__(self, bun, ketchup, sausage):
        self.name = 'Стандартный хот-дог'
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


class VeganHotDog:
    def __init__(self, bun, ketchup, vegan_sausage):
        self.name = 'Веганский хот-дог'
        self.ingredients = [bun, ketchup, vegan_sausage]

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


class SpicyHotDog:
    def __init__(self, bun, mustard, sausage, jalapeno):
        self.name = 'Острый хот-дог'
        self.ingredients = [bun, mustard, sausage, jalapeno]

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

    def add_ingredients(self):
        pass
        # self.ingredients.append(data)
