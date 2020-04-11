# По данным портала открытых данных Москвы определите количество дней, когда
# освещение включено 12 часов или более.

from urllib.request import urlopen
import json

infile = open('input_w09e03.json', 'r', encoding='utf-8')
lstData = json.load(infile)

c = 1
for row in lstData:
    cells = row['Cells']
    duration = cells['DurationOfLighting']
    h, m = duration.split(':')
    if int(h) >= 12:
        c += 1

print(c)