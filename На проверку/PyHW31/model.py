from abc import ABCMeta, abstractmethod
import copy

# Задание
# Создайте приложение для эмуляции работа киоска
# по продаже хот-догов. Приложение должно иметь следующую функциональность:

# 1. Пользователь может выбрать из трёх стандартных
# рецептов хот-дога или создать свой рецепт.

# 2. Пользователь может выбирать добавлять ли майонез,
# горчицу, кетчуп, топпинги (сладкий лук, халапеньо,
# чили, соленный огурец и т.д.).

# 3. Информацию о заказанном хот-доге нужно отображать на экран и сохранять в файл.

# 4. Если пользователь заказывает от трёх хот-догов нужно
# предусмотреть скидку. Скидка зависит от количества
# хот-догов.

# 5. Расчет может производиться, как наличными, так и
# картой.

# 6. Необходимо иметь возможность просмотреть количество проданных хот-догов, выручку, прибыль.

# 7. Необходимо иметь возможность просмотреть информацию о наличии компонентов для создания хот-дога.

# 8. Если компоненты для создания хот-догов заканчиваются нужно вывести информационное сообщение
# о тех компонентах, которые требуется приобрести.

# 9. Классы приложения должны быть построены с учетом принципов SOLID и паттернов проектирования.

class HotDog:
    def __init__(self):
        self.name = None
        self.bun = None
        self.sausage = None

    def __repr__(self):
        return ('\nНазвание хот-дога - {0.name}\n'
                'Булочка - {0.bun}\n'
                'Сосиска - {0.sausage}\n').format(self)

    @abstractmethod
    def add_smth(self):
        pass

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_id(self, sid):
        self.id = sid

    def clone(self):
        return copy.copy(self)


class Chicken(HotDog):
    def __init__(self):
        super().__init__()
        self.name = 'Хот-дог куриный'
        self.bun = 'Молочная'
        self.sausage = 'Куриная'


class Pork(HotDog):
    def __init__(self):
        super().__init__()
        self.name = 'Хот-дог свиной'
        self.bun = 'Сырная'
        self.sausage = 'Свиная'

class Beef(HotDog):
    def __init__(self):
        super().__init__()
        self.name = 'Хот-дог говяжий'
        self.bun = 'Молочная'
        self.sausage = 'Говяжья'



class AddTopping(HotDog):
    def __init__(self, ingredient):
        super().__init__()
        self.ingredient = ingredient


    def topping(self):
        return 'Добавка - {0.ingredient}'.format(self)


















