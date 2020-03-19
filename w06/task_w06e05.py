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

t = fin.read()

c_count = 0
w_count = 0
for c in t:
    if c.isalpha():
        in_the_word = True  # каждая буква принадлежит слову
        c_count += 1
    else:
        if in_the_word: # если true, значит закончилось слово и счетчик можно
                        # увеличить на 1. В противном случае, слово еще и не начиналось
            w_count += 1
            in_the_word = False

lines = list(filter(None, t.split('\n')))
l_count = len(lines)

print('Input file contains:')
print(c_count, 'letters')
print(w_count, 'words')
print(l_count, 'lines')

