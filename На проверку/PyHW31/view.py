import hot_dog, toppings


class ChooseHotDog:
    def __init__(self):
        self.hot_dog = None

    def choose_hot_dog(self):
        self.hot_dog = int(input(f'''Какой хот-дог хотите попробовать?
            1 - Стандартный,
            2 - Мексиканский,
            3 - Веганский
            '''))

    def get_hot_dog(self):
        return self.hot_dog


class ToppingsQuestion:
    def toppings_question(self):
        choice = int(input('''Желаете добавить топпинги?
        1 - Да,
        2 - Нет
        '''))
        return choice


class ChooseTopping:
    def __init__(self):
        self.topping = None
        self.amount = None

    def choose_topping(self):
        toppings_list = toppings.list_making()
        count = 0
        for topping in toppings_list:
            count += 1
            print(f'{count}. {topping}, ({self.amount} штук в наличии.)')
        self.topping = int(input('Введите номер топпинга, который хотите добавить - '))

    def get_topping(self):
        return self.topping


class AddTopping:
    def add_topping(self, hot_dog, topping):
        hot_dog.append(topping)


class Greeting:
    def greeting(self):
        print(f'\nДобро пожаловать в киоск. Я знаю, вы хотите попробовать наши знаменитые хот-доги.\n'
              f'Вы можете выбрать хот-дог из меню или создать свой.\n'
              f'Наши хот-доги:')


class Choice:
    def choice(self):
        choice = int(input('''\nВыберите, что хотите сделать.
        1 - Выбрать хот-дог из меню,
        2 - Создать свой.\n'''))
        return choice


class MakeHotDog:
    def __init__(self):
        self.hot_dog = None

    def set_hot_dog(self):
        self.hot_dog = []

    def add_hot_dog(self, hot_dog):
        for i in hot_dog:
            self.hot_dog.append(i)

    def add_topping(self, topping):
        self.hot_dog.append(topping)

    def get_hot_dog(self):
        return self.hot_dog


def menu():
    greeting = Greeting()
    greeting.greeting()

    choice = Choice()
    choice.choice()

    choose_hot_dog = ChooseHotDog()
    choose_hot_dog.choose_hot_dog()

    topping_question = ToppingsQuestion()
    topping_question.toppings_question()

    choose_topping = ChooseTopping()
    choose_topping.choose_topping()

    new_hot_dog = MakeHotDog()
    new_hot_dog.set_hot_dog()
    new_hot_dog.add_hot_dog(hot_dog.recipes_list.get_list()[choose_hot_dog.get_hot_dog() - 1])
    print(new_hot_dog.get_hot_dog())
    new_hot_dog.add_topping(toppings.list_making()[choose_topping.get_topping() - 1])
    # toppings.
    print(new_hot_dog.get_hot_dog())


menu()
