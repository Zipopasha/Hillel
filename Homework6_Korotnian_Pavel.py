from lib import *
from random import randint

"""Задание 1. В отдельном файле (пусть будет lib.py) написать функцию, которая требует от пользователя ответить да
или нет ( Y/N ) и возвращает True/False в зависимости от того, что он ввел. В основном файле (пусть будет
Homework6_Korotnian_Pavel.py) попросить пользователя ввести с клавиатуры строку и вывести ее на экран. Используя
импортированную из lib.py функцию спросить у пользователя, хочет ли он повторить операцию (Y/N).Повторять пока
пользователь отвечает Y и прекратить когда пользователь скажет N. """

# def foo():
#     user_input_2 = input('Enter the text --> ')
#     print(user_input_2)
#     return choice()
#
#
# while foo():
#     continue

"""Задание 2. Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100) случайное
число и предлагает пользователю его угадать. Пользователь вводит число. Если пользователь не угадал - предлагает
пользователю угадать еще раз, пока он не угадает. Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y -
повторить. N - Прекратить"""

# def game():
#     random_int = randint(1, 100)
#     while True:
#         int_input = int(input('Enter the integer from 1 to 100 --> '))
#         print(random_int)
#         if int_input != random_int:
#             continue
#         elif int_input == random_int:
#             if choice() is True:
#                 return game()
#             else:
#                 print('--------  Game Over  ---------')
#                 break
#
#
# game()

"""Задание 3* Добавить в задание 2 счетчик попыток и диапазон чисел (начало и конец). Пользователь
вводит количество попыток, за которые он может угадать число. Пользователь вводит начало и конец диапазона. На каждом
шаге угадывания числа сообщайте пользователю сколько попыток у него осталось. Если пользователь не смог угадать за
отведенное количество попыток сообщить ему об окончании (Looser!)."""

#
# def game():
#     counter = int(input('Enter the number of tries -->'))
#     min_int = int(input('Enter minimal range -->'))
#     max_int = int(input('Enter maximal range -->'))
#     random_int = randint(min_int, max_int)
#     while counter > 0:
#         int_input = int(input('Enter the integer from ' + str(min_int) + ' to ' + str(max_int) + ' --> '))
#         print(random_int)
#         if int_input != random_int:
#             counter = counter - 1
#             continue
#         elif int_input == random_int:
#             print('--- Congratulations!!! You have guessed the right number!!! -----')
#             if choice() is True:
#                 return game()
#             else:
#                 print('--------  Game Over  ---------')
#                 break
#     print('Looser!')
#
#
# game()

""" Задание 4.** Добавить в задание 2 вывод сообщения-подсказки.
Если пользователь ввел число, и не угадал - сообщать: "Холодно" если разница между загаданным и введенным числами
больше 10, "Тепло" - если от 5 до 10 и "Горячо" если от 4 до 1."""


def game():
    counter = int(input('Enter the number of tries -->'))
    min_int = int(input('Enter minimal range -->'))
    max_int = int(input('Enter maximal range -->'))
    random_int = randint(min_int, max_int)
    while counter > 0:
        int_input = int(input('Enter the integer from ' + str(min_int) + ' to ' + str(max_int) + ' --> '))
        print(random_int)
        if int_input != random_int:
            counter = counter - 1
            continue
        elif int_input == random_int:
            print('--- Congratulations!!! You have guessed the right number!!! -----')
            if choice() is True:
                return game()
            else:
                print('--------  Game Over  ---------')
                break
    print('Looser!')


game()

"""П.С. У вас уже есть знание функций так что все выполнение можно разбить на функции. Постарайтесь чтобы функции 
выполняли только одну задачу. Случайными значениями занимается модуль random (
https://docs.python.org/3/library/random.html) """

"""П.П.С. Очень сильно к карме добавляет проверка введенных значений, причем не только на тип, но и на значение (
включайте логику). """
