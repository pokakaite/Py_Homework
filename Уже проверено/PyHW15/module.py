from random import randint as r

def id(arg):
    x = r(100000000000000, 999999999999999)
    arg.append(x)
    return x

def number(arg):
    x = int(f"{89}{r(100000000, 999999999)}")
    arg.append(x)
    return x

def show(*args):
    print(args[0], ' ' * 16, args[1])

def show1(label, users, l1, l2, x):
    print(f"\n {' ' * 8} Списки, отсортированные по {x}:")
    for i in range(len(l1)):
        print(f"{label[i]} {users[i]} - {l1[i]} - {l2[i]}")
    return ''

def sorted(*args):
    args[0].sort(key=lambda x: x[args[1]])
    sp_sorted1 = [i[1] for i in args[0]]
    sp_sorted2 = [i[2] for i in args[0]]
    sp_sorted3 = [i[3] for i in args[0]]
    print(show1(args[2], sp_sorted1, sp_sorted2, sp_sorted3, args[3]))