# В файле https://stepik.org/media/attachments/lesson/209723/5.html находится
# одна таблица. Просуммируйте все числа в ней. Теперь мы не только добавили
# разных тегов для изменения стиля отображения, но и сделали невалидный HTML-код
# (правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы).
# Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.
#
# Вы можете исправить html-код или попробовать использовать нестандартный парсер
# html, такой как html5lib (вместо html.parser).

from urllib.request import urlopen
from bs4 import BeautifulSoup
import html5lib


resp = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'html5lib')

tds = soup.find_all('td')

sum = 0
for td in tds:
    sum += int(td.string)
print(sum)