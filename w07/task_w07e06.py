# Сейчас вам нужно установить библиотеку BeautifulSoup. Чтобы проверить, что
# всё установилось хорошо, необходимо запусить код, представленный ниже и
# сдать в качестве ответа то, что он выводит.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html') # скачиваем файл
html = resp.read().decode('utf-8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
table = soup.find('table', attrs={'class': 'wikitable sortable'})

cnt = 0
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)
