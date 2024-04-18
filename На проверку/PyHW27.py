import json
# Задание 1
# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицы в качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).


class Packing:
    def __init__(self, group, which, which2):
        self.group = group
        self.which = which
        self.which2 = which2

    def show_dictionary(self):
        print(f'Ваш список - {self.group}')
        print()
        return self.group

    def add_element(self):
        element = input(f"Введите название {self.which} - ")
        city = input(f"Введите название {self.which2} - ")
        print()
        self.group.update({element: city})
        return self.show_dictionary()

    def delete_element(self):
        element = input(f"Введите название {self.which}, которую хотите удалить - ")
        print()
        if element not in self.group:
            print(f"Такой {self.which} нет в списке.\n")
        else:
           self.group.pop(element)
        return self.show_dictionary()

    def find_element(self):
        element = input(f"Введите название {self.which}, которую хотите найти - ")
        count = 0
        for c in self.group:
            count += 1
            if c == element:
                print(f"Наличие такой {self.which} есть в списке и находится под номером {count}\n")
        if element not in self.group:
            print(f"Такой {self.which} нет в списке.\n")
        return self.show_dictionary()

    def edit_element(self):
        element = input(f"Введите название {self.which}, которую хотите редактировать - ")
        if element not in self.group:
            print(f"Такой {self.which} нет в списке.\n")
        else:
            newCountry = input(f"Введите новое название {self.which} - ")
            capital = input(f"Введите новое название {self.which2} - ")
            print()
            self.group[newCountry] = self.group.pop(element)
            self.group[newCountry] = capital

        return self.show_dictionary()

    def save_data(self):
        with open("j.json", "w") as f:
            json.dump(self.group, f)
        return self.show_dictionary()

    def load_data(self):
        with open("j.json", "r") as f:
            self.group = json.load(f)
        print(f'Ваш список - {self.group}\n')
        return self.group

    def menu(self):
        choice = int(input("""Что вы хотите сделать со списком?
        1 - Добавить новые данные,
        2 - Удалить данные,
        3 - Найти данные,
        4 - Редактировать данные,
        5 - Сохранить данные,
        6 - Загрузить данные
        7 - Выйти.
        """))
        if choice == 1:
            self.add_element()
        if choice == 2:
            self.delete_element()
        if choice == 3:
            self.find_element()
        if choice == 4:
            self.edit_element()
        if choice == 5:
            self.save_data()
        if choice == 6:
            self.load_data()
        if choice == 7:
            return
        return self.menu()


group_1 = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'Bulgaria': 'Sofia',
    'Ukraine': 'Kyiv'
}

countries = Packing(group_1, 'страны', 'столицы')
countries.show_dictionary()
countries.menu()


# Задание 2
# Есть некоторый словарь, который хранит названия
# музыкальных групп (исполнителей) и альбомов. Название группы используется в качестве ключа, название
# альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных,
# редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).

group_2 = {
    'Cage The Elephant': 'Social Cues',
    'One Direction': 'Four',
    'Olivia Rodrigo': 'Sour',
    'Dikta': 'Get It Together'
}

albums = Packing(group_2, "исполнителя", "альбома")
albums.show_dictionary()
albums.menu()
