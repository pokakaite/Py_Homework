class Grocery:
    def __init__(self, category, products):
        self.category = category
        self.products = products

    def show(self):
        print(f'\n\t\t{self.category}:')
        for key, value in self.products.items():
            print(f'{key} - {value} рублей', end='\n')

    @staticmethod
    def menu():
        print(f'\nДобро пожаловать в супермаркет "У Кати".\n'
              f'\nНаша продукция:')


meat_list = {
    "Куриное филе": 340,
    "Говядина": 450,
    "Свинина": 400,
    "Сосиски": 150,
    "Куриные ножки": 280
}

grocery_list = {
    "Овсяные хлопья": 120,
    "Подсолнечное масло": 100,
    "Рис": 150,
    "Сахар": 80,
    "Макароны": 70
}

sweets_list = {
    "Шоколад": 69,
    "Печенье": 100,
    "Мармелад": 80,
    "Конфеты": 50,
    "Зефир": 100
}



meat = Grocery('Мясной отдел', meat_list)
grocery = Grocery('Бакалея', grocery_list)
sweets = Grocery("Сладости", sweets_list)

Grocery.menu()
meat.show()
grocery.show()
sweets.show()

