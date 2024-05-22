class ChoiceMaking:
    def make_choice(self, choice, func1=None, func2=None, func3=None):
        match choice:
            case 1:
                func1()
            case 2:
                func2()
            case 3:
                func3()


class ChoiceMaking2:
    def make_choice(self, choice, item, func1=None, func2=None, func3=None):
        match choice:
            case 1:
                func1(item)
            case 2:
                func2(item)
            case 3:
                func3(item)


class WhichDonut:
    choice = None

    @staticmethod
    def set_choice():
        WhichDonut.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return WhichDonut.choice


class IfToppings:
    choice = None

    @staticmethod
    def set_choice():
        print('''\nЖелаете добавить топпинг?
        1 - Да
        2 - Нет''')
        IfToppings.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return IfToppings.choice


class WhichTopping:
    choice = None

    @staticmethod
    def set_choice():
        print('\nВведите номер топпинга, который хотите добавить.')
        WhichTopping.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return WhichTopping.choice


class IfDonut:
    choice = None

    @staticmethod
    def set_choice():
        print('''\nЖелаете попробовать ещё один пончик?
        1 - Да
        2 - Нет''')
        IfDonut.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return IfDonut.choice


class PayChoice:
    choice = None

    @staticmethod
    def set_choice():
        print('''Выберите способ оплаты.
        1 - Наличный расчёт.
        2 - Расчёт по карте.
        ''')
        PayChoice.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return PayChoice.choice
