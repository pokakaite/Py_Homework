import concurrent.futures
import time
import random
from math import factorial


class File:
    def __init__(self):
        self.name = ''

    def set_name(self):
        self.name = input('Введите путь к файлу (пример: "file.txt") - ')

    def get_name(self):
        return self.name


class Numbers:
    def __init__(self):
        self.numbers = []

    def set_numbers(self):
        for number in range(0, 15):
            self.numbers.append(random.randint(1, 15))

    def add_to_file(self, file, numbers):
        with open(file, 'w+') as f:
            for number in numbers:
                f.write(f'{number} ')
        print('Файл заполнился числами.')

    def get_numbers(self, file):
        with open(file, 'r+') as f:
            text = f.read()
            numbers = list(map(int, text.split()))
            return numbers


def simple_numbers(numbers):
    time.sleep(3)

    with open('info.txt', 'a+', encoding='utf-8') as f:
        l = []
        k = 0
        for i in numbers:
            for j in range(2, i):
                if i % j == 0:
                    k = k + 1
            if k == 0:
                l.append(i)
            else:
                k = 0
        f.write(str(f'Простые числа списка - {l}\n'))
    print('Список с простыми числами готов. Откройте файл "info.txt"')


def find_factorial(numbers):
    time.sleep(3)
    print('Список с факториалами чисел готов. Откройте файл "info.txt"')
    with open('info.txt', 'a+', encoding='utf-8') as f:
        for i in numbers:
            f.write(str(f'Факториалы числа {i} равен {factorial(i)}\n'))


def add_info(info):
    time.sleep(3)
    with open('info.txt', 'w+', encoding='utf-8') as f:
        f.write(str(info, '\n'))


numbers = Numbers()
file1 = File()
file1.set_name()
numbers.set_numbers()

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    result1 = executor.submit(numbers.add_to_file, file1.get_name(), numbers.numbers)
    result2 = executor.submit(simple_numbers, numbers.get_numbers(file1.get_name()))
    result3 = executor.submit(find_factorial, numbers.get_numbers(file1.get_name()))

finish = time.perf_counter()
print(f'Процесс закончился спустя {round(finish - start, 2)} секунды')
