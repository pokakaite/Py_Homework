from abc import ABCMeta, abstractmethod
import copy

# Задание 2
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

class Pasta(metaclass=ABCMeta):

    def __init__(self):
        self.typeOf = None
        self.sause = None
        self.adding = None
        self.topping = None
        self.id = None

    def __repr__(self):
        return ('\nТип пасты - {0.typeOf}\n'
                'Добавляем соус {0.sause}\n'
                'Добавляем начинку {0.adding}\n'
                'Добавляем добавку {0.topping}\n').format(self)

    @abstractmethod
    def pasta(self):
        pass

    def add_type_of(self):
        return self.typeOf

    def add_sause(self):
        return self.sause

    def add_adding(self):
        return self.adding

    def add_topping(self):
        return self.topping

    def get_typeOf(self):
        return self.typeOf

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Lasagna(Pasta):
    def __init__(self):
        super().__init__()
        self.typeOf = 'Лазанья'
        self.sause = 'Болоньезе'
        self.adding = 'Мясной фарш'
        self.topping = 'Сыр'

    def pasta(self):
        print('')


class Carbonara(Pasta):
    def __init__(self):
        super().__init__()
        self.typeOf = 'Карбонара'
        self.sause = 'Сливочный соус'
        self.adding = 'Бекон'
        self.topping = 'Сыр'

    def pasta(self):
        print('')

class Pappardelle(Pasta):
    def __init__(self):
        super().__init__()
        self.typeOf = 'Паппарделле'
        self.sause = 'Сливочный соус'
        self.adding = 'Грибы'
        self.topping = 'Пармезан'

    def pasta(self):
        print('')


class Pasta_Cache:

    cache = {}

    @staticmethod
    def load():
        lasagna = Lasagna()
        lasagna.set_id("1")
        Pasta_Cache.cache[lasagna.get_id()] = lasagna

        carbonara = Carbonara()
        carbonara.set_id("2")
        Pasta_Cache.cache[carbonara.get_id()] = carbonara

        pappardelle = Pappardelle()
        pappardelle.set_id("3")
        Pasta_Cache.cache[pappardelle.get_id()] = pappardelle

    @staticmethod
    def get_pasta(sid):
        pasta = Pasta_Cache.cache.get(sid, None)
        return pasta.clone()


def show():
    Pasta_Cache.load()

    lasagna = Pasta_Cache.get_pasta("1")
    print(f'{lasagna.get_id()} - {lasagna.get_typeOf()}')

    carbonara = Pasta_Cache.get_pasta("2")
    print(f'{carbonara.get_id()} - {carbonara.get_typeOf()}')

    pappardelle = Pasta_Cache.get_pasta("3")
    print(f'{pappardelle.get_id()} - {pappardelle.get_typeOf()}')

def view():
    print('Добро пожаловать в наш ресторан. Я знаю, вы хотите попробовать наши знаменитые пасты.\n'
          'Вот вам разные виды на выбор:\n')
    show()
    print()
    choice = input('Введите номер пасты, которую желаете попробовать - ')
    print(Pasta_Cache.cache[choice].__repr__())
    print()
    print("Ваша паста готова. Приятного аппетита!")


if __name__ == '__main__':
    view()