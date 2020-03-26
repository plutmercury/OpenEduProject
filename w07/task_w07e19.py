# В файле https://stepik.org/media/attachments/lesson/258944/New-York.html есть
# несколько таблиц, у которых атрибут class равен wikitable collapsible
# collapsed.
#
# Вам необходимо найти первые три такие таблицы и преобразовать их в
# csv-таблицы. В csv-таблице ячейки должны разделяться запятой, а строки не
# должны окружаться кавычками. Таблицы следует разделять пустой строкой.
#
# Например, для таблиц:
#
# <table>
# <tr><td>a</td><td>b</td></tr>
# <tr><td colspan=2>c</td></tr>
# </table>
#
# <table>
# <tr><td>1</td><td>2</td></tr>
# </table>
# ответ должен выглядеть так:
#
# a,b
# c
#
# 1,2

# Обратите внимание, что в таблице может встречаться тег <tbody>, на который мы
# можем просто не обращать внимания. Также там могут встречаться теги <th>
# (ячейка-заголовок), которые следует интерпретировать так же как теги <td>. Для
# поиска нескольких тегов удобно пользоваться методом find_all, которому в
# качестве параметра передается список строк с нужными названиями тегов.
#
# Чтобы получить содержимое тега td (то что записано от открывающего до
# закрывающего тега), достаточно написать td.text. Лучше удалить все пробельные
# символы в полученной строке с помощью метода strip().

from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib


def to_str(tag):
    return tag.text.strip()


def tbl_to_csv(table):
    rows = table.find_all('tr')
    csv = ''
    for row in rows:
        cells = row.find_all(['th', 'td'])
        csv += ','.join(map(to_str, cells)) + '\n'

    return csv


resp = urlopen('https://stepik.org/media/attachments/lesson/258944/New-York.html')
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table', attrs={'class': 'wikitable collapsible collapsed'})

for i in range(3):
    csv = tbl_to_csv(tables[i])
    print(csv)

