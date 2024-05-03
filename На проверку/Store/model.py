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

class Grocery:
    busket = []
    summ = []
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
    def addToBusket():
        product = input("\nВведите название товара, который добавить в корзину - ")
        amount = int(input("Введите количество товара - "))
        items = []

        for i in products_list:
            for item in i:
                items.append(item)

        if product not in items:
            print(f'\nК сожалению, товар под названием "{product}" не представлен в нашем магазине :(')
        else:
            for i in products_list:
                for item, price in i.items():
                    if product == item:
                        Grocery.busket.append({product: amount})
                        Grocery.summ.append(price * amount)
                        print(f'\nТовар "{product}" добавлен в корзину в количестве {amount} шт.')
                        print(f'Ваша корзина:')
                        count = 0
                        for i in Grocery.busket:
                            count += 1
                            for item, amount in i.items():
                                print(f'{count}. {item} - {amount} шт.')
                        print(f'\nСумма товаров - {sum(Grocery.summ)} рублей.')


meat = Grocery('Мясной отдел', meat_list)
grocery = Grocery('Бакалея', grocery_list)
sweets = Grocery("Сладости", sweets_list)

Grocery.greeting()
meat.show()
grocery.show()
sweets.show()