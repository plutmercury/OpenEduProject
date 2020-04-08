# Вася, открывший заправку в прошлой задаче, разорился. Конкуренция оказалась
# слишком большой. Вася предполагает, что это произошло от того, что теги
# заправки могут быть не только на точке, но и на каком-то контуре. Определите,
# сколько заправок на самом деле (не только обозначенных node, но и way) есть на
# фрагменте карты https://stepik.org/media/attachments/lesson/245681/map2.osm

from bs4 import BeautifulSoup

xml = open('input_w08e01.osm', 'r', encoding='utf8')
soup = BeautifulSoup(xml, 'xml')

count = 0
for node in soup.find_all('node'):
    for tag in node('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            count += 1

for way in soup.find_all('way'):
    for tag in way('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            count += 1

print(count)