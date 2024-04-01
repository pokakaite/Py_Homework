from random import randint as r
# Задание 1
# Есть четыре списка целых. Необходимо их объединить
# в пятом списке. Полученный результат в зависимости от
# выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием линейного поиска.


while 1:
    def sp(*args):
        for i in range(0, 4):
            return [r(args[0], args[1]) for _ in range(0, 5)]
    l1 = sp(0, 10)
    l2 = sp(0, 5)
    l3 = sp(5, 10)
    l4 = sp(5, 15)
    l5 = l1 + l2 + l3 + l4
    print('Задание 1. Новый cписок:', l5)

    print('''Вы хотите отсортировать список по убыванию или возрастанию?
    1 - возрастание.
    2 - убывание. ''')
    user = int(input("Ваш выбор - "))

    def sor(x):
        if x == 1:
            l5.sort()
        elif x == 2:
            l5.sort(reverse=True)
        else:
            raise ValueError
        return l5
    print('Отсортированный список -', sor(user))

    user2 = int(input("Введите любой элемент из списка, а я найду его значение - "))
    l5len = len(l5)
    def val(*args):
        for i in range(0, args[1]):
            if args[0][i] == args[2]:
                return i
        return -1
    res = val(l5, l5len, user2)

    if res == -1:
        print('Элемента нет в списке.', '\n')
    else:
        print('Значение элемента -', res, '\n')

# Задание 2
# Есть четыре списка целых. Необходимо объединить
# в пятом списке только те элементы, которые уникальны
# для каждого списка. Полученный результат в зависимости
# от выбора пользователя отсортировать по убыванию или
# возрастанию. Найти значение, введенное пользователем,
# с использованием бинарного поиска.

    def sp(*args):
            for i in range(0, 4):
                return [r(args[0], args[1]) for _ in range(0, 5)]
    l1 = sp(0, 10)
    l2 = sp(0, 5)
    l3 = sp(5, 10)
    l4 = sp(5, 15)

    l5 = list(set(l1) | set(l2) | set(l3) | set(l4))
    l6 = sorted(l5)
    print('Задание 2. Список с уникальными значениями:', l5)

    print('''Вы хотите отсортировать список по убыванию или возрастанию?
         1 - возрастание.
         2 - убывание. ''')
    user = int(input("Ваш выбор - "))

    def sor(x):
        if x == 1:
            l5.sort()
        elif x == 2:
            l5.sort(reverse=True)
        else:
            raise ValueError
        return l5
    print('Отсортированный список -', sor(user))

    user2 = int(input("Введите любой элемент из списка, а я найду его значение - "))
    mid = len(l5) // 2
    bot = 0
    top = len(l5) - 1

    if l5 == l6:
        while l5[mid] != user2 and bot <= top:
            if user2 > l5[mid]:
                bot = mid + 1
            else:
                top = mid - 1
            mid = (bot + top) // 2

    elif l5 != l6:
        while l5[mid] != user2 and bot <= top:
            if user2 > l5[mid]:
                top = mid - 1
            else:
                bot = mid + 1
            mid = (bot + top) // 2

    if bot > top:
        print('Элемента нет в списке.', '\n')
    else:
        print('Значение элемента -', mid, '\n')