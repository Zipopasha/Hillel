"""Модифицируйте класс Point следующим образом:
обеспечьте проверку значений координат (только числа),
добавьте метод, который бы позволял сравнивать точки (если координаты точек совпадают - точки равны)"""


class Point:
    _x = 0
    _y = 0

    def __init__(self, initial_x, initial_y):
        self.x, self.y = initial_x, initial_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        if type(val) is int:
            self._x = val
        else:
            raise ValueError

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        if type(val) is int:
            self._y = val
        else:
            raise ValueError

    def __str__(self):
        return f'Point with x is {self._x} and y is {self._y}'

    def __add__(self, other):

        if other.__class__ is not self.__class__:
            raise Exception
        return Line(self, other)

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            raise Exception
        else:
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False


p1 = Point(5, 6)
p2 = Point(-3, 15)
p3 = Point(-3, 15)
print(p1)
print(p2)
print(p3)
print(p1 == p2)
print(p2 == p3)

"""Модифицируйте класс Line следующим образом:
обеспечьте проверку точек начала и конца при создании линии в __init__ (точки начала и конца отрезка не должны совпадать)
модифицируйте метод __str__ так чтобы он отдавал информацию в формате ("Line with points [информация о точке начала]
[информация о точке конца] and length [длина]") """


class Line:
    _start_point = Point(0, 0)
    _finish_point = Point(0, 0)

    def __init__(self, first_point, second_point):

        if not isinstance(first_point, Point) or \
                not isinstance(second_point, Point) or \
                not self._check_points_coord(first_point, second_point):
            raise Exception
        self._start_point = first_point
        self._finish_point = second_point

    def length(self):
        return ((self._start_point.x - self._finish_point.x) ** 2 + (
                    self._start_point.y - self._finish_point.y) ** 2) ** 0.5

    @staticmethod
    def _check_points_coord(p1, p2):
        return not (p1.x == p2.x and p1.y == p2.y)

    @classmethod
    def get_default(cls):
        return cls._start_point, cls._finish_point

    def __str__(self):
        return f'Line with points {self._start_point} and {self._finish_point} and length {self.length()}'

    def __getitem__(self, item):  # a['b']
        print(f'in __getitem__ with {item}')
        return getattr(self, item, None)

    def __setitem__(self, item, val):  # a['b'] = c
        print(f'in __setitem__ with {item} {val}')
        return setattr(self, item, val)

    def __eq__(self, other):  # ==
        print(f'{other}')

        if other.__class__ is not self.__class__:
            raise Exception
        return self.length() == other.length()


line1 = Line(p1, p2)
line2 = p1 + p2
print(line1)

"""* Допишите класс Unit: добавьте метод hit, который принимает обьект класса Unit, и наносит ему повреждения. удары 
юнита должны только уменьшать здоровье атакуемого юнита! на величину собственной атаки минус защита атакуемого юнита. 
добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было установить < 0 (например у юнита осталось 5 
здоровья а его ударили на 10) """


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

    def hit(self, enemy):
        enemy.health = enemy.health - (self.damage - enemy.defence)
        if enemy.health <= 0:
            enemy.health = 0
            print('You are dead!')
        else:
            return print(f'Ого ты ёбнул!!! У врага осталось {enemy.health} ХП')


unit_1 = Unit('Gandalf', 100, 50, 10)
unit_1.unit_info()
unit_2 = Unit('Sashka', 80, 60, 15)
unit_2.unit_info()
unit_2.hit(unit_1)
unit_2.hit(unit_1)
unit_1.unit_info()
# print(unit_1.health)
