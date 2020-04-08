# Вам дана область карты
# https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по первым ста node в этой области и выведите для каждого три числа:
# id, широту (атрибут lat) и долготу (атрибут lon).
#
# Числа для каждого node выводите в отдельной строке, разделяя одним пробелом.
# Обрабатывать node нужно в том же порядке, в котором они встречаются во входном
# файле.
#
# Если вы все делаете правильно, то ваш ответ должен начинаться со строк:
#
# 60276311 55.5695795 37.5764692
# 60276312 55.5682232 37.5754573

from bs4 import BeautifulSoup

xml = open('input_w08e11.osm', 'r', encoding='utf8')

soup = BeautifulSoup(xml, 'lxml')

counter = 0

nodes = soup.find_all('node')

for i in range(100):
    node = nodes[i]
    print(node['id'], node['lat'], node['lon'])

