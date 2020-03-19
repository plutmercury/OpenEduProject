# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа в формате, приведенном в примере. Словом
# считается последовательность больших и маленьких латинских букв (для
# проверки того, состоит ли строка только из латинских букв удобно
# пользоваться методом isalpha()). Все остальные символы считаются
# разделителями слов.
#
# Ссылка на входной файл:
# https://stepik.org/media/attachments/lesson/258919/input.txt
#
# Пример входного файла:
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# Пример ответа:
#
# Input file contains:
# 108 letters
# 20 words
# 4 lines

fin = open('input_w06e05.txt', 'r', encoding='utf8')
fout = open('output_w06e05.txt', 'w', encoding='utf8')

t = fin.read()

c_count = 0
for c in t:
    if c.isalpha():
        c_count += 1
    else:
        print(c, end='', file=fout)

fout.close()

w = t.split()
w_count = len(w)

l = t.split('\n')
l_count = len(l) -1

print('Input file contains:')
print(c_count, 'letters')
print(w_count, 'words')
print(l_count, 'lines')