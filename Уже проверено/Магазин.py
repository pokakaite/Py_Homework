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

products_list = meat_list, grocery_list, sweets_list
# summ = ''

class Grocery:
    def __init__(self, category, products):
        self.category = category
        self.products = products

    def show(self):
        print(f'\n\t\t{self.category}:')
        for key, value in self.products.items():
            print(f'{key} - {value} рублей', end='\n')

    @staticmethod
    def greeting():
        print(f'\nДобро пожаловать в супермаркет "У Кати".\n'
              f'\nНаша продукция:')

    @staticmethod
    def menu():
        product = input("\nВведите название товара, который хотите приобрести - ")
        amount = int(input("Введите количество товара - "))

        for i in products_list:
            for item, price in i.items():
                if product == item:
                    # summ += int()
                    print(f'\nТовар "{product}" добавлен в корзину в количестве {amount} шт.')
        else:
            if product not in [i for i in products_list]:
                print(f'\nК сожалению, товар под названием "{product}" не представлен в нашем магазине :(')


        # for i in summ:
        #     i += i
        # print(f'Сумма всех товаров, добавленных в корзину - {i * amount} рублей.')
        # return Grocery.menu()




meat = Grocery('Мясной отдел', meat_list)
grocery = Grocery('Бакалея', grocery_list)
sweets = Grocery("Сладости", sweets_list)

Grocery.greeting()
meat.show()
grocery.show()
sweets.show()
Grocery.menu()

