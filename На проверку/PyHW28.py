import json
import pickle

# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.


class Auto:
    def __init__(self):
        self.name = ''
        self.year = 0
        self.producer = ''
        self.engineCapacity = 0
        self.color = ''
        self.price = 0

    def info(self):
        self.name = input("Введите название модели - ")
        self.year = int(input("Введите год выпуска - "))
        self.producer = input("Введите название производителя - ")
        self.engineCapacity = int(input("Введите объем двигателя автомобиля (в куб. см) - "))
        self.color = input("Введите цвет автомобиля - ")
        self.price = int(input("Введите стоимость автомобиля - "))
        print()

    def defName(self):
        return print(f"Название модели - {self.name}.")
    def defYear(self):
        return print(f"Год выпуска - {self.year} год.")
    def defProducer(self):
        return print(f"Производитель - {self.producer}.")
    def defEngineCapacity(self):
        return print(f"Объем двигателя - {self.engineCapacity} куб. см..")
    def defColor(self):
        return print(f"Цвет автомобиля - {self.color}.")
    def defPrice(self):
        return print(f"Стоимость автомобиля - {self.price} рублей.")

    def intoDict(self):
        Auto = {
            'Название модели': self.name,
            'Год выпуска': self.year,
            'Производитель': self.producer,
            'Объем двигателя': self.engineCapacity,
            'Цвет автомобиля': self.color,
            'Стоимость автомобиля': self.price
        }
        return Auto

    def save_data_json(self):
        info = self.intoDict()
        with open("car.json", 'w') as f:
            json.dump(info, f)

    def load_data_json(self):
        with open("car.json", "r") as f:
            info = json.load(f)
            print(f'Выгруженные данные из json - {info}')
            return info

    def save_data_pickle(self):
        info = self.intoDict()
        with open("car.pkl", 'wb') as f:
            f.write(pickle.dumps(info))

    def load_data_pickle(self):
        with open("car.pkl", 'rb') as f:
            info = pickle.load(f)
            print(f'Выгруженные данные из pickle - {info}')
            return info


car = Auto()
car.info()
car.defName()
car.defYear()
car.defProducer()
car.defEngineCapacity()
car.defColor()
car.defPrice()
car.intoDict()
print()
car.save_data_json()
car.load_data_json()
car.save_data_pickle()
car.load_data_pickle()
print()

# Задание 2
# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных с использованием json и pickle.

class Book:
    def __init__(self):
        self.name = ''
        self.year = 0
        self.publisher = ''
        self.genre = ''
        self.author = ''
        self.price = 0

    def info(self):
        self.name = input("Введите название книги - ")
        self.year = int(input("Введите год выпуска - "))
        self.publisher = input("Введите название издательства - ")
        self.genre = input("Введите жанр - ")
        self.author = input("Введите имя автора - ")
        self.price = int(input("Введите стоимость книги - "))
        print()

    def defName(self):
        return print(f"Название книги - {self.name}.")
    def defYear(self):
        return print(f"Год выпуска - {self.year} год.")
    def defPublisher(self):
        return print(f"Издание - {self.publisher}.")
    def defGenre(self):
        return print(f"Жанр - {self.genre}.")
    def defAuthor(self):
        return print(f"Автор - {self.author}.")
    def defPrice(self):
        return print(f"Стоимость книги - {self.price} рублей.")

    def intoDict(self):
        Auto = {
            'Название книги': self.name,
            'Год выпуска': self.year,
            'Издание': self.publisher,
            'Жанр': self.genre,
            'Автор': self.author,
            'Стоимость книги ': self.price
        }
        return Auto

    def save_data_json(self):
        info = self.intoDict()
        with open("book.json", 'w') as f:
            json.dump(info, f)

    def load_data_json(self):
        with open("book.json", "r") as f:
            info = json.load(f)
            print(f'Выгруженные данные из json - {info}')
            return info

    def save_data_pickle(self):
        info = self.intoDict()
        with open("book.pkl", 'wb') as f:
            f.write(pickle.dumps(info))

    def load_data_pickle(self):
        with open("book.pkl", 'rb') as f:
            info = pickle.load(f)
            print(f'Выгруженные данные из pickle - {info}')
            return info

book = Book()
book.info()
book.defName()
book.defYear()
book.defPublisher()
book.defGenre()
book.defAuthor()
book.defPrice()
book.intoDict()
print()
book.save_data_json()
book.load_data_json()
book.save_data_pickle()
book.load_data_pickle()
print()

# Задание 3
# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

class Stadium:
    def __init__(self):
        self.name = ''
        self.openingDate = ''
        self.country = ''
        self.city = ''
        self.capacity = 0

    def info(self):
        self.name = input("Введите название стадиона - ")
        self.openingDate = input("Введите дату открытия стадиона - ")
        self.country = input("Введите название страны - ")
        self.city = input("Введите название города - ")
        self.capacity = input("Вместительность стадиона - ")
        print()

    def defName(self):
        return print(f"Название стадиона - {self.name}.")
    def defOpeningDate(self):
        return print(f"Дата открытия стадиона - {self.openingDate}.")
    def defCountry(self):
        return print(f"Страна - {self.country}.")
    def defCity(self):
        return print(f"Город - {self.city}.")
    def defCapacity(self):
        return print(f"Вместительность стадиона - {self.capacity} человек.")

    def intoDict(self):
        Auto = {
            'Название стадиона': self.name,
            'Дата открытия стадиона': self.openingDate,
            'Страна': self.country,
            'Город': self.city,
            'Вместительность стадиона': self.capacity,
        }
        return Auto

    def save_data_json(self):
        info = self.intoDict()
        with open("stadium.json", 'w') as f:
            json.dump(info, f)

    def load_data_json(self):
        with open("stadium.json", "r") as f:
            info = json.load(f)
            print(f'Выгруженные данные из json - {info}')
            return info

    def save_data_pickle(self):
        info = self.intoDict()
        with open("stadium.pkl", 'wb') as f:
            f.write(pickle.dumps(info))

    def load_data_pickle(self):
        with open("stadium.pkl", 'rb') as f:
            info = pickle.load(f)
            print(f'Выгруженные данные из pickle - {info}')
            return info

stadium = Stadium()
stadium.info()
stadium.defName()
stadium.defOpeningDate()
stadium.defCountry()
stadium.defCity()
stadium.defCapacity()
stadium.intoDict()
print()
stadium.save_data_json()
stadium.load_data_json()
stadium.save_data_pickle()
stadium.load_data_pickle()
print()