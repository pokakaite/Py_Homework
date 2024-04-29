from model import *
import view

def start():
    view.startView()
    ch = int(input(f"1 - Да; "
                   f"2 - Нет\n"))
    if ch == 1:
        return view.showAllShoes()
    else:
        return view.endView()

if __name__ == "__main__":
    start()