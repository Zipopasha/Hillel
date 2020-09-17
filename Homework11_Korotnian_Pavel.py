"""Подключитесь к API НБУ (https://bank.gov.ua/ua/open-data/api-dev),
 получите текущий курс валют и запишите его в TXT-файл в формате
 "дата создания запроса"
1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
3. [название ввалюты 3] to UAH: [значение курса к валюте 3]
...
n. [название ввалюты n] to UAH: [значение курса к валюте n]"""

import requests

try:
    response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
except:
    pass

with open('Currency.txt', 'w') as f:
    i = 1
    date = response.json()
    f.write('Дата создания запроса:  ' + (date[0]['exchangedate']) + '\n')
    for key in response.json():
        res = '' + str(i) + '. ' + key['txt'] + ' to UAH: ' + str(key['rate']) + '\n'
        i += 1
        f.write(res)

"""2. ** Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны
 к этой валюте за указаную дату используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение. 
 Реализовать с помощью ООП!"""
