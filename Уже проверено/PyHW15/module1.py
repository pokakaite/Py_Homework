def show1(label, l1, l2, x):
    print(f"\n {' ' * 8} Списки, отсортированные по {x}:")
    for i in range(len(l1)):
        print(f"{label[i]} {l1[i]} - {l2[i]}")
    return ''

def sorted(*args):
    args[0].sort(key=lambda x: x[args[1]])
    sp_sorted1 = [i[1] for i in args[0]]
    sp_sorted2 = [i[2] for i in args[0]]
    print(show1(args[2], sp_sorted1, sp_sorted2, args[3]))