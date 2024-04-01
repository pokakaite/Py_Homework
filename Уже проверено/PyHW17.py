# Задание 1
# Создайте программу, хранящую информацию о вели-
# ких баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления,
# удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

basketball_players = {
    "Майкл Джордан": 1.98,
    "Леброн Джеймс": 2.06,
    "Карим Абдул-Джаббар": 2.18,
    "Мэджик Джонсон": 2.06,
    "Коби Брайант": 1.98,
    "Шакил О'Нил": 2.16,
    "Ларри Берд": 2.06,
    "Уилт Чемберлен": 2.16,
    "Билл Расселл": 2.08,
    "Тим Данкан": 2.11
}

def showTheList(basketball_players):
    print('Имя баскетболиста - рост')
    for key, value in basketball_players.items():
        print(f'{key} - {value}м')
showTheList(basketball_players)

def menu():
    choice = int(input('''Что вы хотите сделать со списком?
    1 - Добавить нового баскетболиста в список,
    2 - Удалить баскетболиста из списка,
    3 - Найти, есть ли баскетболист в списке,
    4 - Заменить данные о баскетболисте.
    5 - Перейти к следующему списку.
    Ваш выбор - '''))
    return choice

def addToList(basketball_players):
    newName = input("Введите имя баскетболиста - \n")
    height = input("Введите рост баскетболиста - \n")
    basketball_players.update({newName:height})
    return showTheList(basketball_players)

def deleteFromList(basketball_players):
    which = input("Введите имя и фамилию баскетболиста из списка, чтобы удалить - \n")
    if basketball_players.get(which) == None:
        print('Такого баскетболиста нет в списке.\n')
    else:
        basketball_players.pop(which)
        print("Баскетболист успешно удалён.")
    return showTheList(basketball_players)

def searchThePlayer(basketball_players):
    which = input("Введите имя и фамилию баскетболиста, которого хотите найти - \n")
    list_players = []
    count = 0
    for i in basketball_players.keys():
        list_players.append(i)

    for i in list_players:
        count += 1
        if i == which:
            print(f'{which} есть в списке и находится под номером {count}. Его рост - {basketball_players[which]}м.\n')

    if basketball_players.get(which) == None:
        print('Такого баскетболиста нет в списке.\n')
    return basketball_players

def changeInfo(basketball_players):
    previousName = input("Введите имя и фамилию баскетболиста, чьи данные вы хотите изменить - \n")
    if basketball_players.get(previousName) == None:
        print("Такого баскетболиста нет в списке.\n")
    else:
        newName = input("Введите новые имя и фамилию - \n")
        newHeight = input("Введите рост - \n")
        basketball_players[newName] = basketball_players.pop(previousName)
        basketball_players[newName] = newHeight
    return showTheList(basketball_players)

def changingList(basketball_players):
    choice = menu()
    if choice == 1:
        addToList(basketball_players)
    elif choice == 2:
        deleteFromList(basketball_players)
    elif choice == 3:
        searchThePlayer(basketball_players)
    elif choice == 4:
        changeInfo(basketball_players)
    elif choice == 5:
        print("Пока.\n")
        return
    else:
        showTheList(basketball_players)
    return changingList(basketball_players)
changingList(basketball_players)

# Задание 2
# Создайте программу «Англо-французский словарь».
# Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность до-
# бавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

########################################## Сделала англо-немецкий словарь
dictionary = {
    "Excuse me": "Entschuldigung",
    "Homework": "Hausaufgabe",
    "Welcome": "Willkommen",
    "Cat": "Katze",
    "Dog": "Hund",
    "Stay": "Bleiben",
    "Mother": "Mutter",
    "Holiday": "Urlaub"
}

def showTheList2(dictionary):
    print('Слово на английском - слово на немецком.')
    for key, value in dictionary.items():
        print(f'{key} - {value}')
showTheList2(dictionary)

def menu2():
    choice = int(input('''Что вы хотите сделать со списком?
    1 - Добавить новое слово с переводом в список,
    2 - Удалить слово из списка,
    3 - Найти, есть ли слово в списке,
    4 - Заменить перевод слова.
    5 - Перейти к следующему списку.
    Ваш выбор - '''))
    return choice

def addToList2(dictionary):
    newWord = input("Введите слово - \n")
    translation = input("Введите перевод слова - \n")
    dictionary.update({newWord:translation})
    return showTheList2(dictionary)

def deleteFromList2(dictionary):
    which = input("Введите слово из списка, чтобы удалить - \n")
    if dictionary.get(which) == None:
        print('Такого слова нет в списке.\n')
    else:
        dictionary.pop(which)
        print("Слово успешно удалено.")
    return showTheList2(dictionary)

def searchThePlayer2(dictionary):
    which = input("Введите слово, которое хотите найти - \n")
    list_words = []
    count = 0
    for i in dictionary.keys():
        list_words.append(i)

    for i in list_words:
        count += 1
        if i == which:
            print(f'Слово {which} есть в списке и находится под номером {count}. Его перевод - {dictionary[which]}.\n')

    if dictionary.get(which) == None:
        print('Такого слова нет в списке.\n')
    return dictionary

def changeInfo2(dictionary):
    previousWord = input("Введите слово, которое вы хотите заменить - \n")
    if dictionary.get(previousWord) == None:
        print("Такого слова нет в списке.\n")
    else:
        newWord = input("Введите новое слово - \n")
        newTranslation = input("Введите перевод - \n")
        dictionary[newWord] = dictionary.pop(previousWord)
        dictionary[newWord] = newTranslation
    return showTheList(basketball_players)

def changingList2(dictionary):
    choice = menu2()
    if choice == 1:
        addToList2(dictionary)
    elif choice == 2:
        deleteFromList2(dictionary)
    elif choice == 3:
        searchThePlayer2(dictionary)
    elif choice == 4:
        changeInfo2(dictionary)
    elif choice == 5:
        print("Пока.\n")
        return
    else:
        showTheList2(dictionary)
    return changingList2(dictionary)
changingList2(dictionary)


# Задание 3
# Создайте программу «Фирма». Нужно хранить ин-
# формацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется
# реализовать возможность добавления, удаления, поис-
# ка, замены данных. Используйте словарь для хранения
# информации.

firm = {
    "Данилова Екатерина Александровна": {
        "Номер телефона": 89061025666,
        "E-mail": "danilova.katherine02@gmail.com",
        "Должность": "программист-разработчик",
        "Номер кабинета": 1,
        "Skype": 245474
    },
    "Иванов Семен Сергеевич": {
        "Номер телефона": 88005553535,
        "E-mail": "random.info@yandex.ru",
        "Должность": "уборщик",
        "Номер кабинета": 228,
        "Skype": 747294
    },
    "Хелоу Китти": {
        "Номер телефона": 228228,
        "E-mail": "uneyo.lapki@gmail.com",
        "Должность": "психологическая поддержка",
        "Номер кабинета": 7,
        "Skype": 210483
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
        print("Skype -", value["Skype"], '\n')
showTheList3(firm)

def menu3():
    choice = int(input('''Что вы хотите сделать со списком?
    1 - Добавить нового сотрудника,
    2 - Удалить сотрудника из списка,
    3 - Найти, есть ли сотрудник в списке,
    4 - Изменить данные сотрудника.
    5 - Перейти к следующему списку.
    Ваш выбор - '''))
    return choice

def addToList3(firm):
    newName = input("Введите имя нового сотрудника - \n")
    phoneNumber = int(input("Введите номер телефона сотрудника - \n"))
    email = input("Введите E-mail сотрудника - \n")
    jobTitle = input("Введите должность сотрудника - \n")
    classroom = int(input("Введите номер кабинета сотрудника - \n"))
    skype = int(input("Введите номер скайпа сотрудника - \n"))

    firm.update({
        newName: {
            "Номер телефона": phoneNumber,
            "E-mail": email,
            "Должность": jobTitle,
            "Номер кабинета": classroom,
            "Skype": skype
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
    which = input("Введите имя сотрудника, которого хотите найти - \n")
    list_names = []
    count = 0
    for i in firm.keys():
        list_names.append(i)

    if firm.get(which) == None:
        print('Такого сотрудника нет в списке.\n')

    for i in list_names:
        count += 1
        if i == which:
            print(f'Сотрудник {which} есть в списке и находится под номером {count}. Информация о нём -')
            for key, value in firm[which].items():
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
        5 - Номер скайпа сотрудника.
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
    return showTheList3(firm)

def changingList3(firm):
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
        print("Пока.\n")
        return
    else:
        showTheList3(firm)
    return changingList3(firm)
changingList3(firm)

# Задание 4
# Создайте программу «Книжная коллекция». Нужно
# хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство.
# Требуется реализовать возможность добавления, удале-
# ния, поиска, замены данных. Используйте словарь для
# хранения информации.

library = {
    "Лев Николаевич Толстой": {
        "Название произведения": "Анна Каренина",
        "Жанр": "Роман",
        "Год выпуска": 1875,
        "Количество страниц": 385,
        "Издательство": "АСТ"
    },
    "Александр Сергеевич Грибоедов": {
        "Название произведения": "Горе от ума",
        "Жанр": "Комедия",
        "Год выпуска": 1825,
        "Количество страниц": 256,
        "Издательство": "Бомбора"
    },
    "Иван Александрович Гончаров": {
        "Название произведения": "Обломов",
        "Жанр": "Роман",
        "Год выпуска": 1859,
        "Количество страниц": 322,
        "Издательство": "Альпина"
    },
}

def showTheList4(library):
    print('Книжная коллекция:\n')
    for key, value in library.items():
        print("Имя автора -", key)
        print("Название произведения -", value["Название произведения"])
        print("Жанр -", value["Жанр"])
        print("Год выпуска -", value["Год выпуска"])
        print("Количество страниц -", value["Количество страниц"])
        print("Издательство -", value["Издательство"], '\n')
showTheList4(library)

def menu4():
    choice = int(input('''Что вы хотите сделать со списком?
    1 - Добавить нового автора,
    2 - Удалить автора из списка,
    3 - Найти, есть ли автор в списке,
    4 - Изменить данные о произведении.
    5 - Перейти к следующему списку.
    Ваш выбор - '''))
    return choice

def addToList4(library):
    newAuthor = input("Введите имя нового автора - \n")
    nameOfBook = input("Введите название произведения - \n")
    genre = input("Введите жанр произведения - \n")
    year = int(input("Введите год выпуска произведения - \n"))
    pages = int(input("Введите количество страниц произведения - \n"))
    publishing = input("Введите название издательства - \n")

    library.update({
        newAuthor: {
            "Название произведения": nameOfBook,
            "Жанр": genre,
            "Год выпуска": year,
            "Количество страниц": pages,
            "Издательство": publishing
        }
    })
    return showTheList4(library)

def deleteFromList4(library):
    which = input("Введите имя автора из списка, чтобы удалить - \n")
    if library.get(which) == None:
        print('Такого автора нет в списке.\n')
    else:
        library.pop(which)
        print("Автор успешно удалён.")
    return showTheList4(library)

def searchThePlayer4(library):
    which = input("Введите имя автора, которого хотите найти - \n")
    list_names = []
    count = 0
    for i in library.keys():
        list_names.append(i)

    if library.get(which) == None:
        print('Такого автора нет в списке.\n')

    for i in list_names:
        count += 1
        if i == which:
            print(f'Автор {which} есть в списке и находится под номером {count}. Информация о нём -')
            for key, value in library[which].items():
                print(f'{key} - {value}')
    return library

def changeInfo4(library):
    name = input("Введите имя автора, чьи данные хотите изменить - \n")
    if library.get(name) == None:
        print("Такого автора нет в списке.\n")
    else:
        choice = int(input('''Какие данные хотите изменить?
        1 - Название произведения,
        2 - Жанр,
        3 - Год выпуска,
        4 - Количество страниц,
        5 - Издательство.
        Ваш выбор - '''))
        if choice == 1:
            nameOfBook = int(input("Введите название произведения - \n"))
            library[name].update({"Название произведения":nameOfBook})
        if choice == 2:
            genre = input("Введите жанр произведения - \n")
            library[name].update({"Жанр": genre})
        if choice == 3:
            year = input("Введите год выпуска произведения - \n")
            library[name].update({"Год выпуска": year})
        if choice == 4:
            pages = int(input("Введите количество страниц- \n"))
            library[name].update({"Количество страниц": pages})
        if choice == 5:
            publishing = int(input("Введите название издательства - \n"))
            library[name].update({"Издательство": publishing})
    return showTheList4(library)

def changingList4(library):
    choice = menu4()
    if choice == 1:
        addToList4(library)
    elif choice == 2:
        deleteFromList4(library)
    elif choice == 3:
        searchThePlayer4(library)
    elif choice == 4:
        changeInfo4(library)
    elif choice == 5:
        print("Пока.\n")
        return
    else:
        showTheList4(library)
    return changingList4(library)
changingList4(library)