from module1 import *
# Задание 2
# Написать программу «книги». Создать два списка
# с данными. Один список хранит названия книг, второй -
# годы выпуска. Реализовать меню для пользователя:
# ■ Отсортировать по названию книг;
# ■ Отсортировать по годам выпуска;
# ■ Вывести список книг с названиями и годами выпуска;
# ■ Выход;

sp_book = ["Мастер и Маргарита", "Анна Каренина", "Война и мир", "На дне", "Горе от ума"]
sp_year = ['1967', '1875', '1876', '1902', '1825']
label = ['1.', '2.', '3.', '4.', '5.']

print()
start = True
while start:
    print('''Что вы хотите сделать со списком?
    1 - Вывести список книг с названиями и годами выпуска;
    2 - Отсортировать по названию книг;
    3 - Отсортировать по годам выпуска;
    4 - Выйти.''')

    user = int(input("Ваш выбор - "))
    sp_common = list(zip(label, sp_book, sp_year))

    if user == 1:
        print(f"\n {' ' * 8} Список книг с названиями и годами выпуска:")
        for i in range(len(label)):
            print(f'{label[i]} {sp_book[i]} - {sp_year[i]}')
        print()

    if user == 2:
        sorted(sp_common, 1, label, 'названию книг')

    if user == 3:
        sorted(sp_common, 2, label, 'году выпуска')

    if user == 4:
        start = False
        print("До свидания!")