# подсчет супермаркетов по Москве
from bs4 import BeautifulSoup
from urllib.request import urlopen

minlat = 55.5671
minlon = 37.3611
maxlat = 55.9107
maxlon = 37.8638

dlat = (maxlat - minlat) / 100
dlon = (maxlon - minlon) / 100

for i in range(100):
    for j in range(100):

        nminlat = minlat + dlat * i
        nmaxlat = minlat + dlat * (i + 1)
        nminlon = minlon + dlon * j
        nmaxlon = minlon + dlon * (j + 1)

        response = urlopen('https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nminlon) + '%2C' + str(nminlat) + '%2C' + str(nmaxlon) + '%2C' + str(nmaxlat))
        xml = response.read().decode('utf-8')

        # xml = open('map1.osm', 'r', encoding='utf8').read()
        soup = BeautifulSoup(xml, 'lxml')

        names = {}

        for node in soup.find_all('node'):

            name = ''
            flag = False  # супермаркет не найден

            for tag in node('tag'):

                if tag['k'] == 'shop' and tag['v'] == 'supermarket':
                    flag = True

                if tag['k'] == 'name':
                    name = tag['v']

            if flag:
                if name not in names:
                    names[name] = 0
                names[name] += 1

        smarkets = list(names.items())


        def f(x):
            return -x[1], x[0]


        smarkets.sort(key=f)

        print('Sector:', i, j)
        for now in smarkets:
            print(*now)
