from abc import abstractmethod


# рецепты хот-догов. добавление ингредиентов. вывод информации в консоль


class HotDog:
    def __init__(self):
        self.name = None
        self.ingredients = None

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add_ingredients(self):
        pass



class StandartHotDog:
    def __init__(self):
        self.name = 'Стандартный хот-дог'
        self.price = None

    def ingredients(self, bun, ketchup, sausage):
        self.ingredients = [bun, ketchup, sausage]

    def show(self):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: {self.price}'
        print(f'\n{st}')

    def add_ingredients(self, item):
        self.ingredients.append(item)


class VeganHotDog:
    def __init__(self, bun, ketchup, vegan_sausage):
        self.name = 'Веганский хот-дог'
        self.ingredients = [bun, ketchup, vegan_sausage]

    def show(self):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: '
        print(f'\n{st}')

    def add_ingredients(self, item):
        self.ingredients.append(item)


class SpicyHotDog:
    def __init__(self, bun, mustard, sausage, jalapeno):
        self.name = 'Острый хот-дог'
        self.ingredients = [bun, mustard, sausage, jalapeno]

    def show(self):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: '
        print(f'\n{st}')

    def add_ingredients(self, item):
        self.ingredients.append(item)


class HandMadeHotDog:
    def __init__(self, bun, sausage):
        self.name = 'Сделай сам хот-дог'
        self.ingredients = [bun, sausage]

    def show(self):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: '
        print(f'\n{st}')

    def add_ingredients(self, item):
        self.ingredients.append(item)
