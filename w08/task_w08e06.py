# В OpenStreetMap XML встречаются теги way, которые соответствуют некоторым
# линиям и многоугольникам на карте. Way состоит из списка нодов (точек),
# которые задаются тегами nd вложенными в тег way. Для доступного по ссылке
# https://stepik.org/media/attachments/lesson/245681/map2.osm определите id
# того way, который содержит в себе наибольшее количество нодов. Если таких
# несколько - выведите тот id, который встречается в файле раньше.

from bs4 import BeautifulSoup

xml = open('input_w08e01.osm', 'r', encoding='utf8')
soup = BeautifulSoup(xml, 'xml')

way_id = ''
max_nd = 0

for way in soup.find_all('way'):
    if len(way('nd')) > max_nd:
        way_id = way['id']
        max_nd = len(way('nd'))

print(way_id)
