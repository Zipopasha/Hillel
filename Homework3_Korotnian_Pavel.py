"""Задание 1. Написать алгоритм перехода через улицу. Ваш робот стоит на одной стороне уицы и должен попасть на
другую сторону по пешеходному переходу. Робот может шагать вперед, смотреть по сторонам и вперед. Можно описать как
угодно, хоть блок-схемой, хоть текстом, главное понятно. """

# * Если робот находиться в стране с правосторонним движением. В ином случае Заменить слово "налево" на "напрвао" и
# слово "направо" на "налево". 1. Посмотреть налево. Если машины едущие к роботу есть - стоять на месте и повторить
# операцию 1 через 5 секунд. Если машин едущих к роботу нет - идти вперед до разделительной полосы. 2. Посмотреть
# направо. Если машины едущие к роботу есть - стоять на месте и повторить операцию 1 через 5 секунд. Если машин
# едущих к роботу нет - идти вперед до конца пешеходного перехода.

"""Задание 2. Есть list с данными ( например lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 
'Lorem Ipsum']). Напишите код, который формирует новый list (например lst2), который содержит только 
переменные-строки, которые есть в lst1. """

lst1 = ['1', '2', 3, True, 'False', 5, '6',
        7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) is str:
        lst2.append(i)
print(lst2)

"""Задание 3. Ввести из консоли строку. Определить количество слов в этой строке, которые начинаются на букву "а" (
учтите, что слова могут начинаться с большой буквы). """

lst = input('Предложение с буквами "a" ввести тут ------->').lower().split()
lst2 = []
for i in lst:
    if i.startswith('a'):
        lst2.append(i)
print(len(lst2))

"""Задание 4. Вывести пользователю приветствие ('Hello!'). Спросить у пользователя, хочет ли он повторно его увидеть 
этот текст?. Если пользователь введет Y - повторить приветствие и спросить еще раз (спрашиваем каждый раз как 
пользователь ввел Y). Если если пользователь введет N - прекратить спрашивать. Если пользователь ввел не Y или N - 
переспрашивать, пока не введет Y или N. """

choice = 'y'
while True:
    if choice == 'y':
        print('Hello!')
    elif choice == 'n':
        print('Ну и не надо! Подумаешь!')
        break
    choice = input(
        'If you like to see this message again press "Y"').lower()
