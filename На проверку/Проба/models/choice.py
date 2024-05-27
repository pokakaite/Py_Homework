class Choice:
    def make_choice(self, choice, func1, func2, func3, func4):
        match choice:
            case 1:
                func1()
            case 2:
                func2()
            case 3:
                func3()
            case 4:
                func4()


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
        print('''Желаете добавить топпинг?
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
        print('Введите номер топпинга, который хотите добавить.')
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
        print('''\nВыберите способ оплаты.\n1 - Наличный расчёт.\n2 - Расчёт по карте.''')
        PayChoice.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return PayChoice.choice


class IfMoreOrder:
    choice = None

    @staticmethod
    def set_choice():
        print('''Выберите, что хотите сделать.
        
        1 - Принять еще заказ.
        2 - Посмотреть информацию об остатках продуктов.
        3 - Посмотреть информацию о проданных пончиках, прибыль, выручку.
        4 - Выйти.
        ''')
        IfMoreOrder.choice = int(input('Ваш выбор - '))

    @staticmethod
    def get_choice():
        return IfMoreOrder.choice
