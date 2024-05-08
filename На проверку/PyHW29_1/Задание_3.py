from abc import ABCMeta, abstractmethod
import copy

# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.


class Employees(metaclass=ABCMeta):

    def __init__(self):
        self.name = None
        self.id = None

    @abstractmethod
    def person(self):
        pass

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class DEA(Employees):
    def __init__(self):
        super().__init__()
        self.name = "Данилова Екатерина Александровна"

    def person(self):
        print("Inside DEA::person() method.")


class DIV(Employees):
    def __init__(self):
        super().__init__()
        self.name = "Данилова Ирина Владимировна"

    def person(self):
        print("Inside DIV::person() method.")


class DTA(Employees):
    def __init__(self):
        super().__init__()
        self.name = "Данилова Татьяна Александровна"

    def person(self):
        print("Inside DTA::person() method.")


class Employees_Cache:

    cache = {}

    @staticmethod
    def load():
        dea = DEA()
        dea.set_id("1")
        Employees_Cache.cache[dea.get_id()] = dea

        div = DIV()
        div.set_id("2")
        Employees_Cache.cache[div.get_id()] = div

        dta = DTA()
        dta.set_id("3")
        Employees_Cache.cache[dta.get_id()] = dta

    @staticmethod
    def get_employee(sid):
        employee = Employees_Cache.cache.get(sid, None)
        return employee.clone()


if __name__ == '__main__':
    Employees_Cache.load()

    dea = Employees_Cache.get_employee("1")
    print(dea.get_name())

    div = Employees_Cache.get_employee("2")
    print(div.get_name())

    dta = Employees_Cache.get_employee("3")
    print(dta.get_name())


