# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли
# их строки. Если нет, то вывести несовпадающую строку
# из каждого файла.

f1 = open("file1.txt", "w+", encoding='UTF-8')
f1.write('''Стоимость компании Facebook составляет 1/5 стоимости Microsoft.
Facebook стоит 48 миллиардов долларов,
Microsoft в пять раз больше.
''')

f2 = open("file2.txt", "w+", encoding='UTF-8')
f2.write('''Стоимость компании Facebook составляет 1/5 стоимости Microsoft.
Facebook стоит 96 миллиардов долларов,
Microsoft в пять раз больше.
''')

with open("file1.txt", "w+", encoding='UTF-8') as f1:
     str1 = []
     st = f1.readline()
     while st != "":
          str1.append(st)
          st = f1.readline()

with open("file2.txt", "w+", encoding='UTF-8') as f2:
     str2 = []
     st = f2.readline()
     while st != "":
          str2.append(st)
          st = f2.readline()

for i in range(len(str1)):
     if str1[i] != str2[i]:
          print(f'\nОтличающиеся строки:\n\n'
                f'Строка из первого файла - {str1[i]}\n'
                f'Строка из второго файла - {str2[i]}')

# Задание 2
# Дан текстовый файл. Необходимо создать новый файл
# и записать в него следующую статистику по исходному
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

with open("file1.txt", "r+", encoding='UTF-8') as f1:
     count = 0
     text = f1.read()
     text = text.lower()
     for letters in text:
          count += 1
     res = count

     vowels = 'аоеёуыэяиюeyuioa'
     count1 = 0
     for letters in text:
          for i in vowels:
               if letters == i:
                    count1 += 1
     res1 = count1

     consonants = 'йцкнгшщзхфвпрлджчсмтбqwrtpsdfghjklzxcvbnm'
     count2 = 0
     for letters in text:
          for i in consonants:
               if letters == i:
                    count2 += 1
     res2 = count2

     numbers = '0123456789'
     count3 = 0
     for letters in text:
          for i in numbers:
               if letters == i:
                    count3 += 1
     res3 = count3

     with open("file3.txt", "w+", encoding='UTF-8') as f3:
          f3.write("Статистика по файлу ")
          f3.write(str(f1.name))
          f3.write('\n')
          f3.write("Количество символов: ")
          f3.write(str(res))
          f3.write('\n')
          f3.write('Количество строк: ')
          f3.write(str(len(str1)))
          f3.write('\n')
          f3.write('Количество гласных: ')
          f3.write(str(res1))
          f3.write('\n')
          f3.write('Количество согласных: ')
          f3.write(str(res2))
          f3.write('\n')
          f3.write('Количество цифр: ')
          f3.write(str(res3))
          f3.write('\n')

# Задание 3
# Дан текстовый файл. Удалить из него последнюю
# строку. Результат записать в другой файл.

with open("file1.txt", "r+", encoding='UTF-8') as f1:
     str1 = []
     st = f1.readline()
     while st != "":
          str1.append(st)
          st = f1.readline()

     str1 = str1[:-1]

     with open("file4.txt", "w+", encoding='UTF-8') as f4:
          for i in str1:
               f4.write(i)

# Задание 4
# Дан текстовый файл. Найти длину самой длинной
# строки.

with open("file1.txt", "r+", encoding='UTF-8') as f1:
     str1 = []
     st = f1.readline()
     while st != "":
          str1.append(st)
          st = f1.readline()

     count = 0
     res = []
     for i in range(len(str1)):
          for l in str1[i]:
               count += 1
          res.append(count)
          count = 0

     print(f'Длина самой длинной строки в {f1.name} равна {max(res)}\n')

# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем
# встречается заданное пользователем слово.

with open("file1.txt", "r+", encoding='UTF-8') as f1:
     text = f1.read()
     newText = ""
     count = 0
     for i in text:
          if i[count] != '.' and i[count] != ',':
               newText += i[count]
               count += 1
          count = 0

     newText = newText.replace('\n', ' ')

     word = input("Введите слово, которое хотите найти в файле - ")
     amount = newText.count(word)
     print(f'Количество раз слово {word} встречается в файле {f1.name} - {amount}.')

# Задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется
# пользователем.

with open("file1.txt", "r+", encoding='UTF-8') as f1:
     previousWord = input("Введите слово, которое хотите заменить - ")
     newWord = input("Введите слово с новым содержанием - ")
     text = f1.read()
     newText = ""
     count = 0
     for i in text:
          newText += i[count]

     newText = newText.replace(previousWord, newWord)
     print(f"Перейдите в {f1.name}, чтобы проверить изменения.")
     with open("file1.txt", "w+", encoding='UTF-8') as f1:
          pass
          f1.write(newText)

f1.close()
f2.close()