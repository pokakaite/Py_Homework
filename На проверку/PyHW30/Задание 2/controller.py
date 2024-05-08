import view

def start():
    try:
        return view.showTheRecipe(view.startView())
    except IndexError:
        view.endView()


if __name__ == "__main__":
    start()

