import json
# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).


# Задание 2
# Есть некоторый словарь, который хранит названия
# музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название
# альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных,
# редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).

countries = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'Bulgaria': 'Sofia',
    'Ukraine': 'Kyiv'
}

def showDictionary(countries):
    print(countries)
    print()


def addElement(countries):
    country = input("Введите название страны - ")
    city = input("Введите название столицы - ")
    print()
    countries.update({country: city})
    return showDictionary(countries)

def deleteElement(countries):
    country = input("Введите название страны, которую хотите удалить - ")
    print()
    if country not in countries:
        print("Такой страны нет в списке.\n")
    else:
       countries.pop(country)
    return showDictionary(countries)

def findElement(countries):
    country = input("Введите название страны, которую хотите найти - ")

    count = 0
    for c in countries:
        count += 1
        if c == country:
            print(f"Такая страна есть в списке и находится под номером {count}\n")
    if country not in countries:
        print("Такой страны нет в списке.\n")

    return showDictionary(countries)


def editElement(countries):
    country = input("Введите название страны, которую хотите редактировать - ")
    newCountry = input("Введите новое название страны - ")
    capital = input("Введите новое название столицы - ")
    print()
    countries[newCountry] = countries.pop(country)
    countries[newCountry] = capital

    return showDictionary(countries)

def saveData(countries):
    with open("j.json", "w") as f:
        json.dump(countries, f)
    return showDictionary(countries)

def loadData():
    with open("j.json", "r") as f:
        n = json.load(f)
    print(n, '\n')

def menu():
    choice = int(input("""Что вы хотите сделать со списком?
    1 - Добавить новые данные,
    2 - Удалить данные,
    3 - Найти данные,
    4 - Редактировать данные,
    5 - Сохранить данные,
    6 - Загрузить данные
    """))

    if choice == 1:
        addElement(countries)
    if choice == 2:
        deleteElement(countries)
    if choice == 3:
        findElement(countries)
    if choice == 4:
        editElement(countries)
    if choice == 5:
        saveData(countries)
    if choice == 6:
        loadData()

    return menu()

showDictionary(countries)
menu()









