# Задание 1
# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.

class Figure:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def int(self):
        print(f"Площадь фигуры {self.name} - {self.side * self.side} см.")

    def str(self):
        print(f"Информация о фигуре {self.name}: длина стороны - {self.side}")

class Rectangle(Figure):
    def __init__(self, name, side, side2):
        super().__init__(name, side)
        self.side2 = side2

    def int(self):
        print(f"Площадь фигуры {self.name} - {self.side * self.side2} см.")

    def str(self):
        print(f"Информация о фигуре {self.name}: "
              f"длина одной стороны - {self.side}, второй стороны - {self.side2}.")

class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name, radius)
        self.radius = radius

    def int(self):
        print(f"Площадь фигуры {self.name} - {(self.radius ** self.radius) * 3.14} см.")

    def str(self):
        print(f"Информация о фигуре {self.name}: "
              f"радиус - {self.radius}.")

class Triangle(Figure):
    def __init__(self, name, side, side2):
        super().__init__(name, side)
        self.side2 = side2

    def int(self):
        print(f"Площадь фигуры {self.name} - {(self.side * self.side2) / 2} см.")

    def str(self):
        print(f"Информация о фигуре {self.name}: "
              f"длина одной стороны - {self.side}, второй стороны - {self.side2}.")


class Trapezoid(Figure):
    def __init__(self, name, side, side2, height):
        super().__init__(name, side)
        self.side2 = side2
        self.height = height

    def int(self):
        print(f"Площадь фигуры {self.name} - {((self.side + self.side2) / 2) * self.height} см.")

    def str(self):
        print(f"Информация о фигуре {self.name}: "
              f"длина одной стороны - {self.side}, второй стороны - {self.side2}, "
              f"высота - {self.height}.")

square = Figure("Квадрат", 10)
rectangle = Rectangle("Прямоугольник", 10, 20)
circle = Circle("Круг", 2)
triangle = Triangle("Прямоугольный треугольник", 10, 25)
trapezoid = Trapezoid("Трапеция", 10, 20, 5)



# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).

square.int()
rectangle.int()
circle.int()
triangle.int()
trapezoid.int()
print()
square.str()
rectangle.str()
circle.str()
triangle.str()
trapezoid.str()
print()

# Задание 3
# Создайте базовый класс Shape для рисования плоских
# фигур.

# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.

# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат,
# и размерами этого прямоугольника.

# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.

class Shape:
    figures = []
    def __init__(self, name):
        self.name = name

    @staticmethod
    def Show():
        for i in Shape.figures:
            print(i)

    def Save(self, name):
        with open('file.txt', 'a+', encoding='utf-8') as f:
            f.write(str(name.__dict__))
            f.write('\n')

    @staticmethod
    def Load():
        with open('file.txt', 'r+', encoding='utf-8') as f:
            read = f.read()
            Shape.figures.append(read)

class Square(Shape):
    def __init__(self, name, angle, side):
        super().__init__(self)
        self.name = name
        self.angle = angle
        self.side = side

class Rectangle(Shape):
    def __init__(self, name, angle, side, side2):
        super().__init__(name)
        self.name = name
        self.angle = angle
        self.side = side
        self.side2 = side2

class Circle(Shape):
    def __init__(self, name, coords, radius):
        super().__init__(name)
        self.coords = coords
        self.radius = radius

class Ellipse(Rectangle):
    def __init__(self, name, angle, coords, side, side2):
        super().__init__(name, angle, side, side2)
        self.coords = coords



square = Square("Квадрат", 90, 20)
rectangle = Rectangle("Прямоугольник", 90, 20, 10)
circle = Circle("Круг", 150, 10)
ellipse = Ellipse("Эллипс", 90, 0, 20, 10)

square.Save(square)
rectangle.Save(rectangle)
circle.Save(circle)
ellipse.Save(ellipse)

Shape.Load()
Shape.Show()
