import hot_dog, toppings


class ShowHotDog:
    def __init__(self, id, name, price, recipe):
        self.id = id
        self.name = name
        self.price = price
        self.recipe = recipe

    def show(self):
        print(f'\n{self.id}. {self.name}:')
        for ingredient in self.recipe:
            print(f'\t\t{ingredient}')
        print(f'Цена: {self.price} рублей.')


show_standart = ShowHotDog(hot_dog.standart_id.get_id(),
                           hot_dog.standart_name.get_name(),
                           hot_dog.standart_price.get_price(),
                           hot_dog.standart.get_hot_dog())

show_mexican = ShowHotDog(hot_dog.mexican_id.get_id(),
                          hot_dog.mexican_name.get_name(),
                          hot_dog.mexican_price.get_price(),
                          hot_dog.mexican.get_hot_dog())

show_vegan = ShowHotDog(hot_dog.vegan_id.get_id(),
                        hot_dog.vegan_name.get_name(),
                        hot_dog.vegan_price.get_price(),
                        hot_dog.vegan.get_hot_dog())


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

    def choose_topping(self):
        toppings_list = toppings.list_making()
        count = 0
        for topping in toppings_list:
            count += 1
            print(f'{count} - {topping}')
        self.topping = int(input('Введите номер топпинга, который хотите добавить - '))

    def get_topping(self):
        return self.topping


class GetTopping:
    def __init__(self):
        self.topping = None

    def get_topping(self, list, topping):
        for i in list:
            if i == list[topping - 1]:
                self.topping = i
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


def menu():
    greeting = Greeting()
    greeting.greeting()

    show_standart.show()
    show_mexican.show()
    show_vegan.show()

    choice = Choice()
    choice.choice()

    choose_hot_dog = ChooseHotDog()
    choose_hot_dog.choose_hot_dog()

    topping_question = ToppingsQuestion()
    topping_question.toppings_question()

    choose_topping = ChooseTopping()
    choose_topping.choose_topping()

    get_topping = GetTopping()

    add_topping = AddTopping()
    add_topping.add_topping(hot_dog.recipes_list.get_list()[choose_hot_dog.get_hot_dog() - 1],
                            get_topping.get_topping(toppings.list_making(), choose_topping.get_topping()))
    print(hot_dog.recipes_list.get_list())
    print(hot_dog.standart_recipe())







menu()
