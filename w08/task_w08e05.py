# В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым
# точкам на карте. Ноды могут не только обозначать какой-то точечный объект, но
# и входить в состав way (некоторой линии, возможно замкнутой) и не иметь
# собственных тегов. Для доступного по ссылке
# https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента карты
# посчитайте, сколько всего тегов node не содержат в себе ни одного тега tag
# (первое число в ответе), а сколько содержит хотя бы один тег tag (второе число
# в ответе). Числа введите через пробел.

from bs4 import BeautifulSoup

xml = open('input_w08e01.osm', 'r', encoding='utf8')
soup = BeautifulSoup(xml, 'xml')

no_one_tag = 0
at_least_one_tag = 0

for node in soup.find_all('node'):
    if len(node('tag')) == 0:
        no_one_tag += 1
    else:
        at_least_one_tag += 1

print(no_one_tag, at_least_one_tag)

