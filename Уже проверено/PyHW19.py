import pickle
# Задание 1
# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

firm = {
    "Данилова Екатерина Александровна": {
        "Номер телефона": 89061025666,
        "E-mail": "danilova.katherine02@gmail.com",
        "Должность": "программист-разработчик",
        "Номер кабинета": 1,
        "Skype": 245474,
        "Возраст": 21
    },
    "Иванов Семен Сергеевич": {
        "Номер телефона": 88005553535,
        "E-mail": "random.info@yandex.ru",
        "Должность": "уборщик",
        "Номер кабинета": 228,
        "Skype": 747294,
        "Возраст": 25
    },
    "Хелоу Китти": {
        "Номер телефона": 228228,
        "E-mail": "uneyo.lapki@gmail.com",
        "Должность": "психологическая поддержка",
        "Номер кабинета": 7,
        "Skype": 210483,
        "Возраст": 4
    }
}

def showTheList3(firm):
    print('Информация о сотрудниках фирмы:\n')
    for key, value in firm.items():
        print("Имя сотрудника -", key)
        print("Номер телефона -", value["Номер телефона"])
        print("E-mail -", value["E-mail"])
        print("Должность -", value["Должность"])
        print("Номер кабинета -", value["Номер кабинета"])
        print("Skype -", value["Skype"])
        print("Возраст -", value["Возраст"], '\n')
    return firm

def saveToFile(firm):
    with open("infoAboutEmployees.pkl", "wb") as f:
        pickle.dump(firm, f)
    f.close()
    showTheList3(firm)
    return firm

def fromFile():
    with open("infoAboutEmployees.pkl", "rb") as f:
        firm = pickle.load(f)
    f.close()
    showTheList3(firm)
    return firm

def menu3():
    choice = int(input('''Что вы хотите сделать со списком?
    1 - Добавить нового сотрудника,
    2 - Удалить сотрудника из списка,
    3 - Найти, есть ли сотрудник в списке (по фамилии),
    4 - Изменить данные сотрудника.
    5 - Найти сотрудников по первой букве фамилии.
    6 - Найти сотрудников по возрасту.
    7 - Сохранить информацию в файл.
    8 - Выйти.
    Ваш выбор - '''))
    return choice

def addToList3(firm):
    newName = input("Введите имя нового сотрудника - \n")
    phoneNumber = int(input("Введите номер телефона сотрудника - \n"))
    email = input("Введите E-mail сотрудника - \n")
    jobTitle = input("Введите должность сотрудника - \n")
    classroom = int(input("Введите номер кабинета сотрудника - \n"))
    skype = int(input("Введите номер скайпа сотрудника - \n"))
    age = int(input("Введите возраст сотрудника - \n"))

    firm.update({
        newName: {
            "Номер телефона": phoneNumber,
            "E-mail": email,
            "Должность": jobTitle,
            "Номер кабинета": classroom,
            "Skype": skype,
            "Возраст": age
        }
    })
    return showTheList3(firm)
def deleteFromList3(firm):
    which = input("Введите имя сотрудника из списка, чтобы удалить - \n")
    if firm.get(which) == None:
        print('Такого сотрудника нет в списке.\n')
    else:
        firm.pop(which)
        print("Сотрудник успешно удалён.")
    return showTheList3(firm)

def searchThePlayer3(firm):
    which = input("Введите фамилию сотрудника, которого хотите найти - \n")
    list_names = []
    count = 0
    for i in firm.keys():
        list_names.append(i)

    for i in list_names:
        s = i.split(' ')
        count += 1
        if s[0] == which:
            print(f'Сотрудник {which} есть в списке и находится под номером {count}. Информация о нём -')
            for key, value in firm[list_names[count - 1]].items():
                print(f'{key} - {value}')
    return firm

def changeInfo3(firm):
    name = input("Введите имя и фамилию сотрудника, чьи данные хотите изменить - \n")
    if firm.get(name) == None:
        print("Такого сотрудника нет в списке.\n")
    else:
        choice = int(input('''Какие данные хотите изменить?
        1 - Номер телефона сотрудника,
        2 - E-mail сотрудника,
        3 - Должность сотрудника,
        4 - Номер кабинета сотрудника,
        5 - Номер скайпа сотрудника,
        6 - Возраст сотрудника.
        Ваш выбор - '''))
        if choice == 1:
            phoneNumber = int(input("Введите номер телефона сотрудника - \n"))
            firm[name].update({"Номер телефона":phoneNumber})
        if choice == 2:
            email = input("Введите E-mail сотрудника - \n")
            firm[name].update({"E-mail": email})
        if choice == 3:
            jobTitle = input("Введите должность сотрудника - \n")
            firm[name].update({"Должность": jobTitle})
        if choice == 4:
            classroom = int(input("Введите номер кабинета сотрудника - \n"))
            firm[name].update({"Номер кабинета": classroom})
        if choice == 5:
            skype = int(input("Введите номер скайпа сотрудника - \n"))
            firm[name].update({"Skype": skype})
        if choice == 6:
            age = int(input("Введите возраст сотрудника - \n"))
            firm[name].update({"Возраст": age})
    return showTheList3(firm)

def searchBySurname(firm):
    letter = input("Введите букву - ")
    print(f'Сотрудники, чья фамилия начинается на букву {letter}:\n')
    for i in firm.keys():
        for l in i:
            if l[0] == letter:
                print(i)

def searchByAge(firm):
    age = int(input("Введите возраст сотрудника - "))
    print(f'Сотрудники, чей возраст равен {age}:\n')
    for i, n in firm.items():
        if n["Возраст"] == age:
            print(i)
def changingList3(firm):
    fromFile()
    choice = menu3()
    if choice == 1:
        addToList3(firm)
    elif choice == 2:
        deleteFromList3(firm)
    elif choice == 3:
        searchThePlayer3(firm)
    elif choice == 4:
        changeInfo3(firm)
    elif choice == 5:
        searchBySurname(firm)
    elif choice == 6:
        searchByAge(firm)
    elif choice == 7:
        saveToFile(firm)
    elif choice == 8:
        saveToFile(firm)
        print("Пока.\n")
        return
    else:
        saveToFile(firm)
    return changingList3(firm)
changingList3(firm)