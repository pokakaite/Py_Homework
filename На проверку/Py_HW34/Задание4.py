import os
import concurrent.futures
import time
import shutil

class Directory:
    def __init__(self):
        self.path = ''
        self.word = ''

    def set_path(self):
        self.path = input('Введите путь к директорию - ')

    def set_word(self):
        self.word = input('Введите слово, которое хотите найти - ')

directory = Directory()
directory.set_path()
directory.set_word()

start = time.perf_counter()

