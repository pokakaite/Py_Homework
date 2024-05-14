import random
import time
import getpass


# Задание 2
# Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле
# меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл.
# При реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны.


class File:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def file_info(self):
        with open(self.name, 'w+') as f:
            for i in range(10):
                f.write(str(random.randint(0, 30)))
                f.write(' ')

    def file_update(self):
        time.sleep(10)
        File.file_info(self)
        return File.file_update(self)


class GetNumbers:
    def __init__(self, file):
        self.file = file

    def get_numbers(self):
        with open(self.file, 'r') as f:
            text = f.read()
            return text


class LogFile:
    def __init__(self, name, time, user, numbers):
        self.name = name
        self.time = time
        self.user = user
        self.numbers = numbers

    def __str__(self):
        return self.name

    def log_file(self):
        with open(self.name, 'a+', encoding='UTF-8') as f:
            f.write('Время получения данных - ')
            f.write(str(self.time))
            f.write(', Имя пользователя - ')
            f.write(str(self.user))
            f.write('\n')
            f.write('Набор чисел: ')
            f.write(str(self.numbers))
            f.write('\n\n')


class MakeList:
    def __init__(self, numbers):
        self.numbers = numbers

    def make_list(self):
        text = self.numbers.split(' ')
        text = text[:-1]
        numbers = []
        for i in text:
            numbers.append(int(i))
        return numbers


class ShowNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def show_numbers(self):
        print('Набор чисел из файла:', self.numbers)
        print('Сумма чисел:', sum(self.numbers))
        print('Максимальное число -', max(self.numbers))
        print('Минимальное число -', min(self.numbers))


class TryAgain:
    def __init__(self):
        self.choice = None

    def question(self):
        self.choice = int(input('\nЖелаете разобрать новые числа?\n1 - Да\n2 - Нет\n'))
        return self.choice


def view():
    file = File('file.txt')
    file.file_info()
    file_name = file.__str__()

    numbers = GetNumbers(file_name)
    numbers = numbers.get_numbers()

    log_file = LogFile('logfile.txt', time.time(), getpass.getuser(), numbers)
    log_file.log_file()

    list_numbers = MakeList(numbers)
    list_numbers = list_numbers.make_list()

    numbers = ShowNumbers(list_numbers)
    numbers.show_numbers()

    question = TryAgain()

    if question.question() == 1:
        return view()
    else:
        pass


if __name__ == '__main__':
    view()