# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
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

    def make_List(self):
        sp = self.numbers.split(' ')
        for number in sp:
            number = int(number)
            self.someSet.append(number)

    def make_Set(self):
        sp = self.numbers.split(' ')
        self.someSet = set()
        for number in sp:
            number = int(number)
            self.someSet.add(number)

    def changeSet(self, newElement, deleteElement, showSet, checkElement, replaceElement):
        print(f"Ваш список - {self.someSet}\n")
        choice = int(input('''Что хотите сделать со списком?
        1 - Добавить новое число в список;
        2 - Удалить все вхождения числа из списка;
        3 - Показать содержимое списка;
        4 - Проверить есть ли значение в списке;
        5 - Заменить значение в списке;
        6 - Выйти.\n'''))

        if choice == 1:
            newElement()
        if choice == 2:
            deleteElement()
        if choice == 3:
            showSet()
        if choice == 4:
            checkElement()
        if choice == 5:
            replaceElement()
        if choice == 6:
            pass
        return self.changeSet(newElement, deleteElement, showSet, checkElement, replaceElement)

    def newElement(self):
        newNumber = int(input('Введите число, которое хотите добавить в список - '))
        if newNumber in self.someSet:
            print('Такое число уже есть в списке.\n')
        else:
            self.someSet.append(newNumber)

    def deleteElement(self):
        deletedNumber = int(input('Введите число, которое хотите удалить из списка - '))
        if deletedNumber in self.someSet:
            while deletedNumber in self.someSet:
                self.someSet.remove(deletedNumber)
        else:
            print("Такого числа нет в списке.\n")

    def showSet(self):
        choice = int(input('''Выберите, каким хотите видеть список.
        1 - Показать список с начала;
        2 - Показать список с конца.\n'''))

        if choice == 1:
            print('Список с начала -', self.someSet)
        if choice == 2:
            print('Список с конца -', sorted((self.someSet), reverse=True))

    def checkElement(self):
        choice = int(input('Введите число, которое хотите проверить на наличие в списке - '))
        count = 0
        for c in self.someSet:
            count += 1
            if c == choice:
                print(f"Число {choice} есть в списке и находится под номером {count}\n")
        if choice not in self.someSet:
            print(f"Такого числа нет в списке.\n")

    def replaceElement(self):
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
list.make_List()
list.changeSet(list.newElement, list.deleteElement, list.showSet, list.checkElement, list.replaceElement)

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



# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.
