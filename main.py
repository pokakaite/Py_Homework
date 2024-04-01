# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Auto:
    def __init__(self):
        self.name = ''
        self.year = 0
        self.producer = ''
        self.engineCapacity = 0
        self.color = ''
        self.price = 0

    def info(self):
        car.name = input("Введите название модели - ")
        car.year = int(input("Введите год выпуска - "))
        car.producer = input("Введите название производителя - ")
        car.engineCapacity = int(input("Введите объем двигателя автомобиля (в куб. см) - "))
        car.color = input("Введите цвет автомобиля - ")
        car.price = int(input("Введите стоимость автомобиля - "))
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

car = Auto()
car.info()
car.defName()
car.defYear()
car.defProducer()
car.defEngineCapacity()
car.defColor()
car.defPrice()
print()

# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Book:
    def __init__(self):
        self.name = ''
        self.year = 0
        self.publisher = ''
        self.genre = ''
        self.author = ''
        self.price = 0

    def info(self):
        book.name = input("Введите название книги - ")
        book.year = int(input("Введите год выпуска - "))
        book.publisher = input("Введите название издательства - ")
        book.genre = input("Введите жанр - ")
        book.author = input("Введите имя автора - ")
        book.price = int(input("Введите стоимость книги - "))
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

book = Book()
book.info()
book.defName()
book.defYear()
book.defPublisher()
book.defGenre()
book.defAuthor()
book.defPrice()
print()

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

class Stadium:
    def __init__(self):
        self.name = ''
        self.openingDate = ''
        self.country = ''
        self.city = ''
        self.capacity = 0

    def info(self):
        stadium.name = input("Введите название стадиона - ")
        stadium.openingDate = input("Введите дату открытия стадиона - ")
        stadium.country = input("Введите название страны - ")
        stadium.city = input("Введите название города - ")
        stadium.capacity = input("Вместительность стадиона - ")
        print()

    def defName(self):
        return print(f"Название книги - {self.name}.")
    def defOpeningDate(self):
        return print(f"Дата открытия стадиона - {self.openingDate}.")
    def defCountry(self):
        return print(f"Страна - {self.country}.")
    def defCity(self):
        return print(f"Город - {self.city}.")
    def defCapacity(self):
        return print(f"Вместительность стадиона - {self.capacity} человек.")

stadium = Stadium()
stadium.info()
stadium.defName()
stadium.defOpeningDate()
stadium.defCountry()
stadium.defCity()
stadium.defCapacity()