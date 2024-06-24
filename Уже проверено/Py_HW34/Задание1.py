import concurrent.futures
import time
import random

start = time.perf_counter()


class Numbers:
    def __init__(self):
        self.numbers = []

    def set_numbers(self, secs):
        for number in range(0, 10):
            self.numbers.append(random.randint(0, 10))
        time.sleep(secs)
        print(f'Список заполнился.', end='\n')

    def show(self, secs):
        time.sleep(secs)
        print(f'Список чисел - {self.numbers}', end='\n')

    def get_numbers(self):
        return self.numbers


list_numbers = Numbers()



def sum_numbers(numbers, secs):
    time.sleep(secs)
    print(f'Сумма чисел в списке - {sum(numbers)}.', end='\n')


def average_numbers(numbers, secs):
    time.sleep(secs)
    print(f'Среднее арифмитическое в списке - {sum(numbers) / len(numbers)}.', end='\n')


with concurrent.futures.ThreadPoolExecutor() as executor:
    result1 = executor.submit(list_numbers.set_numbers, 1)
    result2 = executor.submit(list_numbers.show, 2)
    result3 = executor.submit(sum_numbers, list_numbers.get_numbers(), 2)
    result4 = executor.submit(average_numbers, list_numbers.get_numbers(), 2)

finish = time.perf_counter()

print(f'Процесс закончился спустя {round(finish - start, 2)} секунды')
