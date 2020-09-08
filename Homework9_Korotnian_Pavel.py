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

"""Модифицируйте класс Line следующим образом: обеспечьте проверку точек начала и конца (точки начала и конца отрезка 
не должны совпадать) модифицируйте метод str так чтобы он отдавал информацию в формате ("Line with points [информация 
о точке начала] [информация о точке конца] and length [длина]") """


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

    def __str__(self, first_point=None, second_point=None, lenght=None):
        return f'"Line with points {first_point} {second_point} and length {lenght}"'

    def __eq__(self, other):  # ==
        print(f'in __eq__ with {other}')

        if other.__class__ is not self.__class__:
            raise Exception
        return self.length() == other.length()

    @property
    def start_point(self):
        return self._start_point


line1 = Line(p1, p2)

atrname = '_start_point'
res = line1
print('---->', res)

print(line1.length())

line2 = p1 + p2
print(line2.length())

print(line2._check_points_coord(p1, p2))
print(Line._check_points_coord(p1, p2))

res = line2.get_default()
print(res[0], res[1])

# print(line1 == 'line2')
print(line1 == line2)
print('*' * 100)

print(line2.__dict__)
print(line2.start_point)  # line2.__dict__['_start_point']

print(line2.__class__.__dict__)  # line2.__class__.__dict__['_start_point']

"""* Допишите класс Unit: добавьте метод hit, который принимает обьект класса Unit, и наносит ему повреждения. удары 
юнита должны только уменьшать здоровье атакуемого юнита! на величину собственной атаки минус защита атакуемого юнита. 
добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было установить < 0 (например у юнита осталось 5 
здоровья а его ударили на 10) """
