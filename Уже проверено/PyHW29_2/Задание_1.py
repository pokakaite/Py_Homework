from abc import ABC, abstractmethod
from typing import List

# Задание 1
# Создайте реализацию паттерна Command. Протестируйте работу созданного класса


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass


class Chief:
    def prepare_spagetti(self):
        print('Шеф отваривает спагетти.')

    def add_sause(self):
        print('Шеф добавляет соус.')

    def add_adding(self):
        print('Шеф добавляет начинку.')

    def add_topping(self):
        print('Шеф добавляет добавки.')



class PrepareSpagettiCommand(ICommand):
    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_spagetti()


class AddSauseCommand(ICommand):
    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_sause()


class AddAddingCommand(ICommand):
    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_adding()


class AddToppingCommand(ICommand):
    def __init__(self, executor: Chief):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping()



class Cafe:

    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("Не задана очередность выполнения"
                  " команд приготовления пиццы")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    chief = Chief()
    cafe = Cafe()
    cafe.addCommand(PrepareSpagettiCommand(chief))
    cafe.addCommand(AddSauseCommand(chief))
    cafe.addCommand(AddAddingCommand(chief))
    cafe.addCommand(AddToppingCommand(chief))

    cafe.cook()