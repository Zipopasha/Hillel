"""Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC) с
помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является номерным знаком.
Если является номерным знаком - возвращает саму строку. """

import re

auto_numbers = input()


def check_automobile_numbers(input_text):
    tpl = r'[a-zA-Z0-9]{2}[0-9]{4}[A-Z]{2}|\d{2}\s\d{3}-\d{2}[A-Z]{2}'
    regexp = re.compile(tpl)
    res = regexp.findall(input_text)
    if not res:
        return print(None)
    else:
        return print(res)


check_automobile_numbers(auto_numbers)

# 'AA1234BB, 12 123-45AB, a12345BC'
