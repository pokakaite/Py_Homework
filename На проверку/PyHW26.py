# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке,
# нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения).
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

class Set:
    def __init__(self):
        self.numbers = input('Введите числа через пробел - ')
        self.someSet = []

    def make_list(self):
        sp = self.numbers.split(' ')
        for number in sp:
            number = int(number)
            self.someSet.append(number)

    def make_set(self):
        sp = self.numbers.split(' ')
        self.someSet = set()
        for number in sp:
            number = int(number)
            self.someSet.add(number)

    def change_set(self, new_element, delete_element, show_set, check_element, replace_element):
        print(f"Ваш список - {self.someSet}\n")
        choice = int(input('''Что хотите сделать со списком?
        1 - Добавить новое число в список;
        2 - Удалить все вхождения числа из списка;
        3 - Показать содержимое списка;
        4 - Проверить есть ли значение в списке;
        5 - Заменить значение в списке;
        6 - Выйти.\n'''))

        if choice == 1:
            new_element()
        if choice == 2:
            delete_element()
        if choice == 3:
            show_set()
        if choice == 4:
            check_element()
        if choice == 5:
            replace_element()
        if choice == 6:
            return
        return self.change_set(new_element, delete_element, show_set, check_element, replace_element)

    def new_element(self):
        newNumber = int(input('Введите число, которое хотите добавить в список - '))
        if newNumber in self.someSet:
            print('Такое число уже есть в списке.\n')
        else:
            self.someSet.append(newNumber)

    def delete_element(self):
        deletedNumber = int(input('Введите число, которое хотите удалить из списка - '))
        if deletedNumber in self.someSet:
            while deletedNumber in self.someSet:
                self.someSet.remove(deletedNumber)
        else:
            print("Такого числа нет в списке.\n")

    def show_set(self):
        choice = int(input('''Выберите, каким хотите видеть список.
        1 - Показать список с начала;
        2 - Показать список с конца.\n'''))

        if choice == 1:
            print('Список с начала -', self.someSet)
        if choice == 2:
            print('Список с конца -', sorted((self.someSet), reverse=True))

    def check_element(self):
        choice = int(input('Введите число, которое хотите проверить на наличие в списке - '))
        count = 0
        for c in self.someSet:
            count += 1
            if c == choice:
                print(f"Число {choice} есть в списке и находится под номером {count}\n")
        if choice not in self.someSet:
            print(f"Такого числа нет в списке.\n")

    def replace_element(self):
        oldNumber = int(input("Введите число, которое хотите заменить - "))
        choice = int(input('''
        1 - Заменить первое вхождение числа,
        2 - Заменить все вхождения числа.
        '''))
        newNumber = int(input("Введите новое число - "))
        if choice == 1:
            if oldNumber in self.someSet:
                self.someSet.remove(oldNumber)
                self.someSet.append(newNumber)
        if choice == 2:
            while oldNumber in self.someSet:
                self.someSet.remove(oldNumber)
                self.someSet.append(newNumber)



list = Set()
list.make_list()
list.change_set(list.new_element, list.delete_element, list.show_set, list.check_element, list.replace_element)

# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.

class Stack:
    def __init__(self):
        self.st = []
        self.size = 0 ### размер стэка

    def push_in_stack(self):
        if self.size:
            if len(self.st) >= self.size:
                print(f'Ваш Стэк - {self.st}\n')
                print(f'Стэк заполнен.\n')
            else:
                string = input('Введите текст - ')
                self.st.append(string)
                print(f'Ваш Стэк - {self.st}\n')
        else:
            string = input('Введите текст - ')
            self.st.append(string)
            print(f'Ваш Стэк - {self.st}\n')

    def pull_out_of_stack(self):
        self.st.pop()
        print(f'Ваш Стэк - {self.st}\n')

    def count_strings(self):
        print(f'Количество строк в Стэке - {len(self.st)}.\n')

    def if_stack_empty(self):
        if (self.st == []) == True:
            print(f'Стэк пустой.\n')
        else:
            print(f'Стэк не пустой.\n')

    def if_stack_full(self):
        if self.size:
            if len(self.st) == self.size:
                print(f'Стэк полный.\n')
            else:
                print(f'Стэк неполный.\n')
        else:
            if self.st == []:
                print(f'Стэк неполный.\n')
            else:
                print(f'У вашего Стэка нефиксированный размер.\n')

    def clear_stack(self):
        self.st.clear()
        print(f'Ваш Стэк - {self.st}\n')

    def get_last_index(self):
        if self.st != []:
            copy = self.st.copy()
            print(f'Значение из списка - {copy.pop()}')
            print(f'Ваш Стэк - {self.st}\n')
        else:
            print(f'Ваш Стэк пустой. Не получается получить значение.\n')

    def menu(self):
        choice = int(input('''Что вы хотите сделать со стэком?
        1 - Поместить строку в стэк,
        2 - Вытолкнуть строку из стэка,
        3 - Подсчитать количество строк в стэке,
        4 - Проверить, пустой ли стэк,
        5 - Проверить, полный ли стэк,
        6 - Очистить стэк,
        7 - Получить значение, не выталкивая верхнюю строку из стэка,
        8 - Выйти.
        '''))

        if choice == 1:
            self.push_in_stack()
        if choice == 2:
            self.pull_out_of_stack()
        if choice == 3:
            self.count_strings()
        if choice == 4:
            self.if_stack_empty()
        if choice == 5:
            self.if_stack_full()
        if choice == 6:
            self.clear_stack()
        if choice == 7:
            self.get_last_index()
        if choice == 8:
            return

        return self.menu()


stack = Stack()
stack.size = 3 ### размер стэка. Можно удалить строку, и тогда размер будет нефиксированный
stack.menu()

# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.


stack2 = Stack()
stack2.menu()