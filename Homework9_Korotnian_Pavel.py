"""Модифицируйте класс Point следующим образом:
обеспечьте проверку значений координат (только числа),
добавьте метод, который бы позволял сравнивать точки (если координаты точек совпадают - точки равны)"""


class Point:
    _x = 0
    _y = 0

    def __init__(self, initial_x, initial_y):
        self._x = initial_x
        self._y = initial_y

    @property
    def x(self):
        if type(self._x) is not int:
            raise ValueError
        else:
            return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        if type(self._y) is not int:
            raise ValueError
        else:
            return self._y

    @y.setter
    def y(self, val):
        self._y = val

    def __str__(self):
        return f'Point with x is {self._x} and y is {self._y}'

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            raise Exception
        else:
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False


p1 = Point(4, 'qqq')
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
                not isinstance(second_point, Point):
            raise Exception

        self._start_point = first_point
        self._finish_point = second_point


"""* Допишите класс Unit: добавьте метод hit, который принимает обьект класса Unit, и наносит ему повреждения. удары 
юнита должны только уменьшать здоровье атакуемого юнита! на величину собственной атаки минус защита атакуемого юнита. 
добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было установить < 0 (например у юнита осталось 5 
здоровья а его ударили на 10) """
