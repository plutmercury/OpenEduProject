# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет
# изучить количество заправок в интересующем его районе. Вася скачал
# интересующий его кусок карты OSM
# https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать,
# сколько на нём отмечено точечных объектов (node), являющихся заправкой. В
# качестве ответа вам необходимо вывести одно число - количество АЗС.
#
# Заправка в OSM обозначается парой ключ-значение amenity=fuel. Эта пара
# находится среди тегов tag внутри node.

from bs4 import BeautifulSoup

xml = open('input_w08.osm', 'r', encoding='utf8')
soup = BeautifulSoup(xml, 'xml')

count = 0
for node in soup.find_all('node'):
    for tag in node('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            count += 1

print(count)