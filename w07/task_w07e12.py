# В этой задаче вам необходимо посчитать количество внутренних
# ссылок, которые есть в обеих статьях:
# https://stepik.org/media/attachments/lesson/258943/Moscow.html и
# https://stepik.org/media/attachments/lesson/258944/New-York.html
#
# Обратите внимание, что если ссылка встречается в статье несколько раз, то
# учитывать ее нужно лишь однажды, т.е. необходимо найти количество различных
# страниц википедии, на которых есть ссылка как из первой, так и из второй статьи.

from urllib.request import urlopen
from bs4 import BeautifulSoup


def list_unique_external_links(url):
    resp = urlopen(url)
    html = resp.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    all_a = soup.find_all('a')

    ext_links = set()
    for a in all_a:
        if a.has_attr('href'):
            href = a['href']

            if not href.startswith('http://') and \
                    not href.startswith('https://') and \
                    ':' not in href and \
                    not href.startswith('#') and \
                    not href.startswith('//'):
                ext_links.add(href)

    return ext_links


ext_links_1 = list_unique_external_links('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
ext_links_2 = list_unique_external_links('https://stepik.org/media/attachments/lesson/258944/New-York.html')

print(len(ext_links_1 & ext_links_2))
