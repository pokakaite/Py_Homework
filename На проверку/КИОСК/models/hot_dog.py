from abc import abstractmethod


class HotDog:
    def __init__(self):
        self.name = None
        self.ingredients = None

    def show(self, price):
        st = f'{self.name}. Состав: '
        for ingredient in self.ingredients:
            st += f'{ingredient.name}, '
        st = st[:-2]
        st += '.'
        st += f'\nСтоимость: {price}'
        print(st)

    @abstractmethod
    def add_ingredients(self):
        pass


class StandartHotDog(HotDog):
    def __init__(self, bun, ketchup, sausage):
        super().__init__()
        self.name = 'Стандартный хот-дог'
        self.ingredients = [bun, ketchup, sausage]

    def add_ingredients(self):
        pass


class VeganHotDog(HotDog):
    def __init__(self, bun, ketchup, vegan_sausage):
        super().__init__()
        self.name = 'Веганский хот-дог'
        self.ingredients = [bun, ketchup, vegan_sausage]

    def add_ingredients(self):
        pass


class SpicyHotDog(HotDog):
    def __init__(self, bun, mustard, sausage, jalapeno):
        super().__init__()
        self.name = 'Острый хот-дог'
        self.ingredients = [bun, mustard, sausage, jalapeno]

    def add_ingredients(self):
        pass


class HandMadeHotDog(HotDog):
    def __init__(self, bun, sausage):
        super().__init__()
        self.name = 'Сделай сам хот-дог'
        self.ingredients = [bun, sausage]

    def add_ingredients(self):
        pass
        # self.ingredients.append(data)
