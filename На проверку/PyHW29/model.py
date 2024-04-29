class Shoes:
    def __init__(self, type_of, kind, color, price, producer, size):
        self.type_of = type_of
        self.kind = kind
        self.color = color
        self.price = price
        self.producer = producer
        self.size = size

    def info(self):
        shoe = {"Тип": self.type_of,
                "Вид": self.kind,
                "Цвет": self.color,
                'Цена': self.price,
                'Производитель': self.producer,
                'Размер': self.size
        }
        return shoe

shoe1 = Shoes("Женская", "Туфли", "Чёрный", 5000, "Гуччи", 39)
shoe2 = Shoes("Мужская", "Кроссовки", "Серый", 4000, "Адидас", 42)

shoes = []
shoes.append(shoe1.info())
shoes.append(shoe2.info())
