from random import randint as r

print()
l1 = [r(0, 20) for _ in range(0, 10)]
l2 = [r(0, 20) for _ in range(0, 10)]
l3 = [r(0, 20) for _ in range(0, 10)]
l4 = l1 + l2 + l3

s1 = set(l1)
s2 = set(l2)
s3 = set(l3)
s4 = set(l4)
print(f"Кортеж 1 - {s1}\nКортеж 2 - {s2}\nКортеж 3 - {s3}")

# Задание 1
# Есть три кортежа целых чисел необходимо найти
# элементы, которые есть во всех кортежах.

print()
print("Элементы, которые есть во всех кортежах:")
for i in s4:
    print(i, end=' ')
print()

# Задание 2
# Есть три кортежа целых чисел необходимо найти
# элементы, которые уникальны для каждого списка.

print('\n')
def uniq_elem(*args):
    uniq = []
    for i in args[0]:
        if i not in args[1] and i not in args[2]:
            uniq.append(i)
    print(f"Элементы, которые уникальны для списка {args[3]}:")
    for i in uniq:
        print(i, end=' ')
    print('\n')

uniq_elem(s1, s2, s3, 1)
uniq_elem(s2, s1, s3, 2)
uniq_elem(s3, s1, s2, 3)

# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы, которые есть в каждом из кортежей и находятся
# в каждом из кортежей на той же позиции.

s1 = (1, 5, 8, 10, 2)
s2 = (2, 7, 8, 11, 4)
s3 = (1, 10, 8, 9, 15)

print(f"Кортеж 1 - {s1}\nКортеж 2 - {s2}\nКортеж 3 - {s3}")

print('Элементы, которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции:')
res = []
for i in range(len(s1)):
    if s1[i] == s2[i] == s3[i]:
        res.append(s1[i])
for i in res: print(i)