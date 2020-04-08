# подсчет супермаркетов по Москве
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from math import cos, pi

DEBUG = True

minlat = 55.5671
minlon = 37.3611
maxlat = 55.9107
maxlon = 37.8638


def distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2

    return (((lat2 - lat1) * 111.3) ** 2 +
            ((lon2 - lon1) * 111.3 * cos(lat1 * pi / 180)) ** 2) ** 0.5


dlat = (maxlat - minlat) / 100
dlon = (maxlon - minlon) / 100

if DEBUG:
    cols = 5
    rows = 5
else:
    cols = 100
    rows = 100

for i in range(cols):
    for j in range(rows):

        roads = {}

        nminlat = minlat + dlat * i
        nmaxlat = minlat + dlat * (i + 1)
        nminlon = minlon + dlon * j
        nmaxlon = minlon + dlon * (j + 1)

        # response = urlopen('https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nminlon) + '%2C' + str(nminlat) + '%2C' + str(nmaxlon) + '%2C' + str(nmaxlat))
        # xml = response.read().decode('utf-8')
        # if not DEBUG:
        urlretrieve('https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nminlon) + '%2C' + str(nminlat) + '%2C' + str(nmaxlon) + '%2C' + str(nmaxlat), 'osm/map_' + str(i) + '-' + str(j) + '.osm')

        xml = open('osm/map_' + str(i) + '-' + str(j) + '.osm', 'r', encoding='utf8').read()

        # xml = open('map1.osm', 'r', encoding='utf8').read()
        soup = BeautifulSoup(xml, 'lxml')

        nodes = {}

        for node in soup.find_all('node'):
            lat = float(node['lat'])
            lon = float(node['lon'])
            id = int(node['id'])
            nodes[id] = (lat, lon)

        for way in soup.find_all('way'):

            flag = False

            for tag in way('tag'):
                if tag['k'] == 'highway':
                    rtype = tag['v']
                    flag = True

            if flag:
                nds = []
                for nd in way('nd'):
                    ref = int(nd['ref'])
                    nds.append(ref)

                for k in range(len(nds) - 1):
                    coord1 = nodes[nds[k]]
                    coord2 = nodes[nds[k + 1]]
                    if rtype not in roads:
                        roads[rtype] = 0
                    roads[rtype] += distance(coord1, coord2)

        print('Sector', i, j)
        for now in roads:
            print(now, roads[now])