import os
import concurrent.futures
import time

class Directory:
    def __init__(self):
        self.path = ''
        self.word = ''

    def set_path(self):
        self.path = input(r'Введите путь к директорию - ')

    def set_word(self):
        self.word = input('Введите слово, которое хотите найти - ')

directory = Directory()
directory.set_path()
directory.set_word()
path = os.path.normpath(directory.path)

start = time.perf_counter()

def find_word(path, word):
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isfile(new_path):
            with open(new_path, 'r+', encoding='utf-8') as f:
                text = f.read()
                if word in text:
                    with open('files.txt', 'a+', encoding='utf-8') as f1:
                        f1.write(f'{text}\n')
    print('\nСодержимое файлов успешно скопировано и отображено в файле "files.txt".')

def remove_word(path):
    time.sleep(2)
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isfile(new_path):
            with open(new_path, 'r+', encoding='utf-8') as f:
                text = f.read()
                with open('ЗапрещенныеСлова.txt', 'r+', encoding='utf-8') as f1:
                    words = f1.read()
                    words = words.split('\n')
                    for word in words:
                        if word in text:
                            text = text.replace(word, '')
                            with open(new_path, 'w+', encoding='utf-8') as f2:
                                f2.write(text)
    print('\nЗапрещенные слова успешно удалены.')

with concurrent.futures.ThreadPoolExecutor() as executor:
    result1 = executor.submit(find_word, path, directory.word)
    result2 = executor.submit(remove_word, path)

finish = time.perf_counter()

print(f'\nПроцесс закончился спустя {round(finish - start, 2)} секунды')