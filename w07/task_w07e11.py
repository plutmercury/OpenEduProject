# В этой задаче достаточно обернуть в функцию то, что делает предыдущая и
# вызвать подсчет числа внутренних ссылок для двух статей:
# https://stepik.org/media/attachments/lesson/258943/Moscow.html и
# https://stepik.org/media/attachments/lesson/258944/New-York.html
#
# В качестве ответа на задачу введите два числа через пробел.

from urllib.request import urlopen
from bs4 import BeautifulSoup


def count_external_links(url):
    resp = urlopen(url)
    html = resp.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    all_a = soup.find_all('a')

    ext_links = []
    for a in all_a:
        if a.has_attr('href'):
            href = a['href']

            if not href.startswith('http://') and \
                    not href.startswith('https://') and \
                    ':' not in href and \
                    not href.startswith('#') and \
                    not href.startswith('//'):
                ext_links.append(href)

    return len(ext_links)


ext_links_1 = count_external_links('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
ext_links_2 = count_external_links('https://stepik.org/media/attachments/lesson/258944/New-York.html')

print(ext_links_1, ext_links_2)
