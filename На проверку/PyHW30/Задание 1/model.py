# Задание 1
# Создайте класс Обувь. Необходимо хранить следующую информацию:
# ■ тип обуви;
# ✓мужская,
# ✓женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Обувь и код для использования модели, контроллера и представления.


class Shoes:
    shoes = []
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
        Shoes.shoes.append(shoe)
        return shoe


heels = Shoes("Женская", "Туфли", "Чёрный", 5000, "Гуччи", 39)
sneakers = Shoes("Мужская", "Кроссовки", "Серый", 4000, "Адидас", 42)
ballet_shoes = Shoes("Женская", "Балетки", "Белый", 500, "Вдохновение", 36)

heels.info()
sneakers.info()
ballet_shoes.info()