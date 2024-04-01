# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеариф-
# метическое каждой группы.

while 1:
    try:
        x = int(input("Введите начало диапазона (больше 0) - "))
        y = int(input("Введите конец диапазона (больше 0) - "))

        if x == 0:
            raise ValueError

        if y == 0:
            raise ValueError

        sum1 = 0
        div2 = 0
        for i in range(x, y + 1):
            if i % 2 == 0:
                sum1 += i
                div2 += 1
        print("Сумма четных чисел -", sum1, ", Среднее арифмитическое -", (sum1 / div2))

        sum2 = 0
        div3 = 0
        for i in range(x, y + 1):
            if i % 2 != 0:
                sum2 += i
                div3 += 1
        print("Сумма нечетных чисел -", sum2, ", Среднее арифмитическое -", (sum2 / div3))

        sum3 = 0
        div9 = 0
        for i in range(x, y + 1):
            if i % 9 == 0:
                sum3 += i
                div9 += 1
        print("Сумма чисел кратных 9 -", sum3, ", Среднее арифмитическое -", (sum3 / div9))

    except ValueError:
        print("Вы ввели неправильное значение.")
    except TypeError:
        print("Вы ввели неправильное значение.")
    except Exception:
        print("Невозможно посчитать")
    else:
        print("All good")
    finally:
        print("End")

# Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
#               %
#               %
#               %
#               %
#               %

    try:
        x = int(input("Введите длину линии - "))
        y = input("Введите символ, который хотите отобразить - ")

        if y == '':
            raise ValueError

        if x == '':
            raise ValueError

        m = [y for _ in range(x)]
        for i in m:
            print('\t\t', i, end="\n")


    except ValueError:
        print("Вы ввели неправильное значение.")
    except TypeError:
        print("Вы ввели неправильное значение.")
    except Exception:
        print("Неверные данные")
    else:
        print("All good")
    finally:
        print("End")

    # Задание 3
    # Пользователь вводит с клавиатуры числа. Если число
    # больше нуля нужно вывести надпись «Number is positive»,
    # если меньше нуля «Number is negative», если равно нулю
    # «Number is equal to zero». Когда пользователь вводит
    # число 7, программа прекращает свою работу и выводит
    # на экран надпись «Good bye!»

    try:
        x = int(input("Введите число - "))

        while x != 7:
            if x > 0:
                print("Number is positive")
            if x < 0:
                print("Number is negative")
            if x == 0:
                print("Number is equal to zero")
            x = int(input("Введите число - "))

        if x == 7:
            print("Good bye!")

    except ValueError:
        print("Вы ввели неправильное значение.")
    except TypeError:
        print("Вы ввели неправильное значение.")
    except Exception:
        print("Неверные данные")
    else:
        print("All good")
    finally:
        print("End")

# Задание 4
# Пользователь вводит с клавиатуры числа. Програм-
# ма должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»

    try:
        x = int(input("Введите число - "))
        sum1 = 0
        numbers = []
        while x != 7:
            sum1 += x
            numbers.append(x)
            minNum = numbers[0]
            maxNum = numbers[0]
            for number in numbers:
                if number < minNum:
                    minNum = number
            for number in numbers:
                if number > maxNum:
                    maxNum = number
            print("Сумма чисел -", sum1)
            print("Минимальное число -", minNum)
            print("Максимальное число -", maxNum)
            x = int(input("Введите число - "))

        if x == 7:
            print("Good bye!")

    except ValueError:
        print("Вы ввели неправильное значение.")
    except TypeError:
        print("Вы ввели неправильное значение.")
    except Exception:
        print("Неверные данные")
    else:
        print("All good")
    finally:
        print("End")