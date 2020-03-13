# Дан список стран и городов каждой страны. Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится.
#
# Программа получает на вход количество стран N. Далее идет N строк, каждая
# строка начинается с названия страны, затем идут названия городов этой
# страны. В следующей строке записано число M, далее идут M запросов —
# названия каких-то M городов, перечисленных выше.
#
# Для каждого из запроса выведите название страны, в котором находится данный
# город.
#
# Sample Input:
#
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Odessa
# 3
# Odessa
# Moscow
# Novgorod
#
# Sample Output:
#
# Ukraine
# Russia
# Russia
# Bye

N = int(input())  # количество стран

cities_countries = {}
for _ in range(N):
    country_cities = input().split()
    for i in range(1, len(country_cities)):
        cities_countries[country_cities[i]] = country_cities[0]

M = int(input()) # количество городов

cities = []
for _ in range(M):
    cities.append(input())

for city in cities:
    if city in cities_countries:
        print(cities_countries[city])

