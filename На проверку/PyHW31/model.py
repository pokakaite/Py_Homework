class HotDog:
    def __init__(self, name, bun, sausage, sause, topping):
        self.name = name
        self.bun = bun
        self.sausage = sausage
        self.sause = sause
        self.topping = topping

    def get_hot_dog(self):
        hot_dog = {
            'Название': self.name,
            'Булочка': self.bun,
            'Сосиска': self.sausage,
            'Соус': self.sause,
            'Добавка': self.topping
        }
        return hot_dog


class RecipeName:
    names = []

    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def add_to_names(self):
        RecipeName.names.append(self.name)


class Standart(RecipeName):
    def __init__(self):
        super().__init__()
        self.name = 'Стандартный'


class Mexican(RecipeName):
    def __init__(self):
        super().__init__()
        self.name = 'Мексиканский'


class Vegan(RecipeName):
    def __init__(self):
        super().__init__()
        self.name = 'Веганский'


class Bun:
    buns = []
    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def add_to_buns(self):
        Bun.buns.append(self.name)


class Wheat(Bun):
    def __init__(self):
        super().__init__()
        self.name = 'Пшеничная'


class Rye(Bun):
    def __init__(self):
        super().__init__()
        self.name = 'Цельнозерновая ржаная мука'

class Sausage:
    sausages = []

    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def add_to_sausages(self):
        Sausage.sausages.append(self.name)


class Milky(Sausage):
    def __init__(self):
        super().__init__()
        self.name = 'Молочная'


class Vegan_Sausage(Sausage):
    def __init__(self):
        super().__init__()
        self.name = 'Соевая'


class Sause:
    sauses = []

    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def add_to_sauses(self):
        Sause.sauses.append(self.name)


class Mayo(Sause):
    def __init__(self):
        super().__init__()
        self.name = 'Майонез'


class Ketchup(Sause):
    def __init__(self):
        super().__init__()
        self.name = 'Кетчуп'


class Mustard(Sause):
    def __init__(self):
        super().__init__()
        self.name = 'Горчица'


class Toppings:
    toppings = []

    def __init__(self):
        self.name = None

    def get_name(self):
        return self.name

    def add_to_toppings(self):
        Toppings.toppings.append(self.name)


class Onion(Toppings):
    def __init__(self):
        super().__init__()
        self.name = 'Лук'


class Jalapeno(Toppings):
    def __init__(self):
        super().__init__()
        self.name = 'Халапеньо'


class Pickles(Toppings):
    def __init__(self):
        super().__init__()
        self.name = 'Маринованные огурцы'
