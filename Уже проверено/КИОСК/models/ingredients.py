from abc import abstractmethod


# информация о цене и количестве ингредиентов. вывод информации.
# менюшка для вывода по очереди.

class Ingredients:
    def __init__(self):
        self.name = None
        self.price = None
        self.amount = None

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def add(self):
        pass


class BunIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Булочка'
        self.price = 10
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class SausageIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Сосиска'
        self.price = 20
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class VeganSausageIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Соевая сосиска'
        self.price = 40
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class KetchupIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Кетчуп'
        self.price = 10
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class MustardIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Горчица'
        self.price = 10
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class MayonaiseIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Майонез'
        self.price = 10
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1



class PickleIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Маринованный огурец'
        self.price = 10
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class OnionIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Лук'
        self.price = 10
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class JalapenoIngredient(Ingredients):
    def __init__(self):
        super().__init__()
        self.name = 'Халапеньо'
        self.price = 20
        self.amount = 1

    def show(self):
        print(f'{self.name} - {self.price} руб. ({self.amount} порция)')

    def add(self):
        self.amount += 1


class ShowIngredients(Ingredients):
    items = []
    def get_items(self, *items):
        for item in items:
            ShowIngredients.items.append(item)

    def show(self):
        print()
        count = 0
        for item in ShowIngredients.items:
            count += 1
            print(f'{count} - ', end='')
            item.show()
