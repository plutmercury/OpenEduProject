# Вам дана область карты
# https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по всем way в этой области, выделите среди них замкнутые (те, у
# которых совпадает ссылка на первый и последний node), среди всех замкнутых
# выделите те, у которых установлен tag с ключом building и произвольным
# значением.
#
# Запомните id для way и список кортежей, содержащих координаты (широту и
# долготу) всех node, входящих в этот way.
#
# Вам предложена функция, которая определяет нечто похожее на площадь замкнутой
# ломаной.
#
# import math
#
# def getsqr(coordlist):
#      baselat = coordlist[0][0]
#      baselon = coordlist[0][1]
#      degreelen = 111300
#      newcoord = []
#      for now in coordlist:
#           newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
#      sqr = 0
#      for i in range(len(newcoord) - 1):
#           sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
#      sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
#      return abs(sqr)
#
# Она принимает на вход список с координатами точек так, как вы выводили его в
# предыдущей задаче (обратите внимание, что числа внутри кортежей должны иметь
# тип float).
#
# С помощью этой функции найдите id для самого большого площади здания.

from bs4 import BeautifulSoup

import math


def getsqr(coordlist):

    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]

    return abs(sqr)


xml = open('input_w08e11.osm', 'r', encoding='utf8')

soup = BeautifulSoup(xml, 'lxml')

nodes = {}
for node in soup.find_all('node'):
    nodes[node['id']] = (float(node['lat']), float(node['lon']))

max_square = 0
max_square_id = 0

for way in soup.find_all('way'):

    flag = False

    nd_refs = []

    # Собираем refs всех nd для way
    for nd in way('nd'):
        nd_refs.append(nd['ref'])

    # Если первая и последняя nd совпадают, значит way замкнутый
    if nd_refs[0] == nd_refs[-1]:

        # ищем для замкнутого way tag c k='building'
        for tag in way('tag'):
            if tag['k'] == 'building':
                flag = True

    if flag:

        nd_coords = []
        for ref in nd_refs:
            nd_coords.append(nodes[ref])

        square = getsqr(nd_coords)
        if square > max_square:
            max_square = square
            max_square_id = way['id']

print(max_square_id)