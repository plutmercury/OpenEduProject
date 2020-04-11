# Дана строка. Если в этом числе буква f встречается только один раз, выведите
# её индекс. Если она встречается два и более раз, выведите индекс её первого и
# последнего появления через пробел. Если буква f в данной строке не
# встречается, ничего не выводите.
#
# Для решения задачи могут быть полезны методы:
#
# string.find(substring) - возвращает позицию самого левого вхождения подстроки
# substring в строку string или -1, если подстрока не найдена
#
# string.rfind(substring) - возвращает позицию самого правого вхождения
# подстроки substring в строку string или -1, если подстрока не найдена
#
# Sample Input:
#
# comfort
#
# Sample Output:
#
# 3

def func(s):
    result = ''

    first = s.find('f')

    if first >= 0:
        last = s.rfind('f')
        if first != last:
            result = str(first) + ' ' + str(last)
        else:
            result = str(first)

    return result


s = input()

print(func(s))

