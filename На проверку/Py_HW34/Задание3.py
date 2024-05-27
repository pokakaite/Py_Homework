import os
import time
import concurrent.futures
import shutil


class Directory:
    def __init__(self):
        self.path = ''

    def set_path(self):
        self.path = input('Введите путь к директорию - ')

    def get_path(self):
        return self.path


class NewDirectory:
    def __init__(self):
        self.name = ''

    def set_path(self, old_dir):
        self.name = input('Введите название новой директории - ')
        parent_dir = old_dir
        path = os.path.join(parent_dir, self.name)
        os.mkdir(path)
        time.sleep(2)
        print(f'Директория {self.name} создана: {os.listdir()}')


    def get_path(self):
        return self.name


directory = Directory()
directory.set_path()

new_directory = NewDirectory()
new_directory.set_path(directory.get_path())

start = time.perf_counter()


def get_from_directory(dir, new_dir):
    time.sleep(3)
    for f in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, f)):
            shutil.copy(os.path.join(dir, f), os.path.join(new_dir, f))
        if os.path.isdir(os.path.join(dir, f)):
            os.system(f'rd /S /Q {new_dir}\\{f}')
            shutil.copytree(os.path.join(dir, f), os.path.join(new_dir, f))

    print('Файлы успешно скопированы в новую директорию.')


with concurrent.futures.ThreadPoolExecutor() as executor:
    result = executor.submit(get_from_directory, directory.get_path(), new_directory.get_path())

finish = time.perf_counter()

print(f'Процесс закончился спустя {round(finish - start, 2)} секунды')
