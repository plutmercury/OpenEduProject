# В файле https://stepik.org/media/attachments/lesson/209723/3.html находится
# одна таблица. Просуммируйте все числа в ней и введите в качестве ответа одно
# число - эту сумму. Для доступа к ячейкам используйте возможности
# BeautifulSoup.

from urllib.request import urlopen
from bs4 import BeautifulSoup


resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tds = soup.find_all('td')

sum = 0
for td in tds:
    sum += int(td.string)

print(sum)