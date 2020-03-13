# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
# парному ему слову. Все слова в словаре различны. Для одного данного слова
# определите его синоним.
#
# Программа получает на вход количество пар синонимов N. Далее следует N строк,
# каждая строка содержит ровно два слова-синонима. После этого следует одно
# слово.
#
# Программа должна вывести синоним к данному слову.
#
# Sample Input:
#
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
#
# Sample Output:
#
# Bye

N = int(input())

dict_direct = {}
for _ in range(N):
    key, value = tuple(input().split())
    dict_direct[key] = value

dict_reverse = {}
for key in dict_direct:
    dict_reverse[dict_direct[key]] = key

word = input()

if word in dict_direct:
    print(dict_direct[word])
elif word in dict_reverse:
    print(dict_reverse[word])
