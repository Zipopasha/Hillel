""" Задание 1.Напишите класс Unit, реализуйте в нем атрибуты "имя", "здоровье", "атака", "защита". Обеспечьте
передачу в "имя" только строчных данных, в "здоровье", "атака", "защита" - только числовых """

import time


class Unit:
    _name = 'Yoda'
    _health = 100
    _damage = 50
    _defence = 30

    def __init__(self, initial_name=None, initial_health=None, initial_damage=None, initial_defence=None):
        if initial_name is not None:
            self.name = initial_name
        if initial_health is not None:
            self.health = initial_health
        if initial_damage is not None:
            self.damage = initial_damage
        if initial_health is not None:
            self.defence = initial_defence

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self._name = val
        else:
            raise Exception('Введите строку в поле Имя')

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if isinstance(val, int):
            self._health = val
        else:
            raise Exception('Введите число в поле Здоровье')

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, val):
        if isinstance(val, int):
            self._damage = val
        else:
            raise Exception('Введите число в поле Урон')

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, val):
        if isinstance(val, int):
            self._defence = val
        else:
            raise Exception('Введите число в поле Защита')

    def unit_info(self):
        print(f'Имя: {self.name}. Здоровье: {self.health} ХП. Урон: {self.damage} ДПС. Защита: {self.defence}.')


unit_1 = Unit('Gandalf', 666, 777, 888)
unit_1.unit_info()

"""Задание 2.Напишите декоратор, замеряющий время выполнения функции"""

start = time.time()
time.sleep(0.1)


def time_decorator(__init__):
    def wrapper(*args, **kwargs):
        res = __init__(*args, **kwargs)
        return res

    return wrapper


finish = time.time()
result = finish - start
print("Время выполнения функции: " + str(result) + " секунд.")


"""Задание 3. * Модифицируйте декоратор таким образом, чтобы декоратор вместе с ответом функции возвращал строку, 
содержащую информацию о затраченном на выполнение времени. Формат возвращаемого времени - H-MM-SS-MS ( 
часы-минуты-секунды-милисекунды) """
