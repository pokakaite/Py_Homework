# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.


# class HTML_Element:
#     def __init__(self):




# Задание 2
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты. Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.


# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.



# Abstract course
class Course:

    def __init__(self):
        self.Fee()
        self.available_batches()

    def Fee(self):
        raise NotImplementedError

    def available_batches(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)










# concrete course
class DSA(Course):
    """Class for Data Structures and Algorithms"""

    def Fee(self):
        self.fee = 8000

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"


# concrete course
class SDE(Course):
    """Class for Software Development Engineer"""

    def Fee(self):
        self.fee = 10000

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"


# concrete course
class STL(Course):
    """Class for Standard Template Library"""

    def Fee(self):
        self.fee = 5000

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"











# Complex Course
class ComplexCourse:

    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)


# Complex course
class Complexcourse(ComplexCourse):

    def Fee(self):
        self.fee = 7000

    def available_batches(self):
        self.batches = 6


# construct course
def construct_course(cls):
    course = cls()
    course.Fee()
    course.available_batches()

    return course  # return the course object


# main method
if __name__ == "__main__":
    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course
    stl = STL()  # object for STL course

    complex_course = construct_course(Complexcourse)
    print(complex_course)


class Phone:
    def __init__(self):
        self.os = None
        self.camera = None
        self.battery = None
        self.screen = None

class PhoneBuilder:
    def __init__(self):
        self.phone = Phone()

    def set_os(self, os):
        self.phone.os = os
        return self

    def set_camera(self, camera):
        self.phone.camera = camera
        return self

    def set_battery(self, battery):
        self.phone.battery = battery
        return self

    def set_screen(self, screen):
        self.phone.screen = screen
        return self

    def get_phone(self):
        return self.phone


builder = PhoneBuilder()
phone = builder.set_os("Android").set_camera("12 MP").set_battery("3500 mAh").set_screen("6.2 inches").get_phone()
