import time
import tkinter
# Задание 1
# Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.

print()
def SimpleNumbers(t):
    def Start():
        start = int(input("Введите начало диапазона - "))
        return start

    def End():
        end = int(input("Введите конец диапазона - "))
        return end

    sp = []
    k = 0
    before = t()
    for i in range(Start(), End() + 1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            sp.append(i)
        else:
            k = 0
    print(f'Простые числа в диапазоне: {sp}')
    after = t()
    print(f"Для вычисления простых чисел понадобилось - {after - before} секунд.")

@SimpleNumbers
def Time():
    t = time.time()
    time.sleep(2)
    return t

print()


# Задание 2
# Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.

#Добавила

# Задание 3
# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос
# отчетности для организаций.

def Reports(organization):
    def info():
        info = '''Отчёт за месяц Апрель:
        Выручка - 1500000 рублей,
        Себестоимость продаж - 1000000 рублей,
        Прибыль - 500000 рублей...
        '''
        return info

    organization(info())
@Reports ################## отчёт в формате файла
def file(info):
    with open('file1.txt', 'w+', encoding='UTF-8') as f1:
        f1.write(info)

@Reports ################## отчёт в формате вывода в консоль
def forPython(info):
    print(info)

@Reports ################## отчёт в формате вывода в TK.
def table(info):
    root = tkinter.Tk()
    root.geometry("600x600+800+100")
    text = tkinter.Label(text=info, background="white", font=("", 20))
    text.pack()
    root.mainloop()