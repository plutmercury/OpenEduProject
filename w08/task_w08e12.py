# Вам дана область карты
# https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по всем way в этой области, выделите среди них замкнутые (те, у
# которых совпадает ссылка на первый и последний node), среди всех замкнутых
# выделите те, у которых установлен tag с ключом building и произвольным
# значением.
#
# Для каждого подходящего под условия way выведите его id по одному в строке.
#
# Если вы все делаете правильно, то ваш ответ должен начинаться со строк
#
# 28889642
# 28911067

from bs4 import BeautifulSoup

xml = open('input_w08e11.osm', 'r', encoding='utf8')

soup = BeautifulSoup(xml, 'lxml')

for way in soup.find_all('way'):
    flag = False

    nd = way('nd')
    if nd[0]['ref'] == nd[len(nd) - 1]['ref']:

        for tag in way('tag'):
            if tag['k'] == 'building':
                flag = True

    if flag:
        print(way['id'])
