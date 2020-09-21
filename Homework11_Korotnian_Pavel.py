"""Подключитесь к API НБУ (https://bank.gov.ua/ua/open-data/api-dev), получите текущий курс валют
 и запишите его в TXT-файл в формате - "дата создания запроса"
1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
3. [название ввалюты 3] to UAH: [значение курса к валюте 3]...
n. [название ввалюты n] to UAH: [значение курса к валюте n]"""

import requests

# import json
# import datetime

# url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
# res = requests.get(url)
#
# posts = json.loads(res.content)
#
#
# def file_write(posts):
#     with open('Currency.txt', 'w') as f:
#         date = datetime.date.today()
#         result = ""
#         i = 0
#         f.write("Дата создания запроса:  " + date.strftime("%d/%m/%Y\n") + "\n")
#         for key in (posts):
#             i += 1
#             result += f"{i}. {key['txt']} to UAH: {key['rate']}\n"
#         f.write(result)
#
#
# def check(posts):
#     try:
#         file_write(posts)
#     except:
#         raise Exception
#
#
# check(posts)
#
try:
    response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
except:
    raise Exception


def currency_check():
    if response.status_code != 200:
        raise Exception
    # elif response.headers != 'application/json':
    #     raise Exception
    else:
        with open('Currency.txt', 'w') as f:
            date = response.json()
            res = ''
            f.write('Дата создания запроса:  ' + (date[0]['exchangedate']) + '\n')
            for key in (response.json()):
                res = '' + str(key['txt'] + ' to UAH: ' + str(key['rate']) + '\n')
                f.write(str(enumerate(res)))
            f.write(res)


currency_check()

"""2. ** Пользователь вводит название валюты и дату, программа возвращает пользователю курс гривны
 к этой валюте за указаную дату используя API НБУ. Формат ввода пользователем данных - на ваше усмотрение. 
 Реализовать с помощью ООП!"""
