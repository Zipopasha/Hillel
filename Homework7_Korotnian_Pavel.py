"""Задание 1. Создайте класс "животное". Наполните его данными и методами на свое усмотрение. Пропишите в методах класса
докстринги с описанием метода"""


def display_count():
    print('Всего Животных: %d' % Animal.ani_count)


class Animal:
    """Базовый класс для всех Животных"""
    ani_count = 0
    animal_type = 'Хомяк'
    weight = 0.2
    height = 5

    def __init__(self, animal_type, weight, height):
        """Функция, по умолчанию создаюая параметры Животных"""
        self.animal_type = animal_type
        self.weight = weight
        self.height = height
        Animal.ani_count += 1

    print(__init__.__doc__)

    def display_animal(self):
        """Функция, отображающая Вид животного, его Вес и Рост"""
        print('Вид: {}. Вес: {} кг. Рост {} см'.format(self.animal_type, self.weight, self.height))

    print(display_animal.__doc__)


# Это создаст первый объект класса Animal
ani1 = Animal("Слон", 2000, 300)

# Это создаст второй объект класса Animal
ani2 = Animal("Жираф", 500, 500)

# Это создаст третий объект класса Animal
ani3 = Animal("Кот", 5, 35)

ani1.display_animal()
ani2.display_animal()
ani3.display_animal()
print("Всего Животных: %d" % Animal.ani_count)

"""Задание 2. Почитайте про Диаграммы класса. Опишите с помощью классов кухонную технику в виде диаграммы. 
Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов. * Описать все то же с 
помощью питона."""


class KitchenAppliances:
    place = 'Kitchen'
    item_name = ''
    state = 0

    def __init__(self, initial_name=None) -> object:
        print(f'Kitchen__init__ {initial_name}')
        if self.state is False:
            self.state_on = False
        if self.state is True:
            self.state = True
        self.item_name = initial_name

    def onoff(self):
        if self.state:
            print('ON')
        else:
            print('OFF')


class BoilingAppliances(KitchenAppliances):





kitchen_app = KitchenAppliances('Електрочайник')
kitchen_app.onoff()
