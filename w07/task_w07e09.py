# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит
# статью с Википедии про язык Python. В этой статье есть теги code, которыми
# выделяются конструкции на языке Python. Вам нужно найти все строки,
# содержащиеся между тегами <code> и </code> и найти те строки, которые
# встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.
#
# Например, если исходный текст страницы выглядел бы так:
#
# <code>a</code>
# <a>bracadabr</a>
# <code>c</code>
# <code>b</code>
# <code>b</code>
# <code>c</code>

# то в ответ надо было бы ввести строку "b c".

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')
html = resp.read().decode('utf-8')
#html = '<code>a</code>' \
#       '<a>bracadabr</a>' \
#       '<code>c</code>' \
#       '<code>b</code>' \
#       '<code>b</code>' \
#       '<code>c</code>'

soup = BeautifulSoup(html, 'html.parser')

code_strings = soup.find_all('code')

text_dict = {}
for s in code_strings:
    if s.string in text_dict:
        text_dict[s.string] += 1
    else:
        text_dict[s.string] = 1

count_dict = {}
for text, count in text_dict.items():
    if count in count_dict:
        count_dict[count].append(text)
    else:
        count_dict[count] = [text]

print(*sorted(count_dict[sorted(count_dict, reverse=True)[0]]))
