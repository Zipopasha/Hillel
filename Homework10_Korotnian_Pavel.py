"""Задание 1. Создайте итератор (обьект класса), который будет возвращать числа фибоначчи"""


class FibonacciIterator:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.fib1 = 0
        self.fib2 = 1
        return self

    def __next__(self):
        fib = self.fib1
        if fib > self.limit:
            raise StopIteration
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return fib


iterator = FibonacciIterator(100)
for i in iterator:
    print(i, end=' ')

"""Задание 2. Создайте генератор (функцию), который будет возвращать числа фибоначчи"""


def fibonacci_generator(fib):
    fib1, fib2 = 0, 1
    for fib in range(fib):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


generator = fibonacci_generator(10)
for i in generator:
    print('\n', *generator)
