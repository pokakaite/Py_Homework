# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.


class Pasta:
    def __init__(self):
        self.typeOf = None
        self.sause = None
        self.adding = None
        self.topping = None

    def __repr__(self):
        return ('Тип - {0.typeOf}\n'
                'Соус - {0.sause}\n'
                'Начинка - {0.adding}\n'
                'Добавка - {0.topping}\n').format(self)

class PastaBuilder(Pasta):
    def add_type_of(self):
        self.typeOf = 'Карбонара'
        return self.typeOf

    def add_sause(self):
        self.sause = 'Сливки'
        return self.sause

    def add_adding(self):
        self.adding = 'Бекон'
        return self.adding

    def add_topping(self):
        self.topping = 'Натертый сыр'
        return self.topping

class Director:
    def construct_pasta(self, builder):
        pasta = builder()
        pasta.add_type_of()
        pasta.add_sause()
        pasta.add_adding()
        pasta.add_topping()

        return pasta

if __name__ == "__main__":
    director = Director()
    complex_pasta = director.construct_pasta(PastaBuilder)
    print(complex_pasta)