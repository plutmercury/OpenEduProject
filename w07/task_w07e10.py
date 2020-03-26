# Мы сохранили статью с википедии, она доступна по ссылке
# https://stepik.org/media/attachments/lesson/258943/Moscow.html
#
# Вам необходимо обработать ее с помощью BeautifulSoup и подсчитать все
# внутренние ссылки, которые не содержат в себе двоеточия (не являются ссылкой
# на техническую статью в википедии) и не начинаются с символа #.
#
# Под ссылкой понимается содержимое аттрибута href тега a. Ссылка называется
# внешней, если она ведет на другой сайт (т.е. начинается с http:// или
# https://). Все остальные ссылки являются внутренними.
#
# Вам могут быть полезны методы find_all для супа (он позволяет найти все теги
# на странице), метод has_attr для тега (проверяет есть ли такой атрибут у
# тега) и доступ к атрибуту тега по аналогии со словарем.
#
# В качестве ответа выведите количество внутренних ссылок, удовлетворяющих
# условию.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

a = soup.find_all('a')

ext_links = []
for link in a:
    if link.has_attr('href'):
        href = link['href']

        if not href.startswith('http://') and \
                not href.startswith('https://') and \
                not ':' in href and \
                not href.startswith('#') and \
                not href.startswith('//'):
            ext_links.append(href)

print(len(ext_links))
