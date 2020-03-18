# В качестве ответа введите все строки наибольшей длины из входного файла, не
# меняя их порядок.
#
# В данной задаче удобно считать список строк входного файла целиком при
# помощи метода readlines().
#
# Ссылка на входной файл:
# https://stepik.org/media/attachments/lesson/258920/input.txt
#
# Пример входного файла:
#
# One
# Twenty one
# Two
# Twenty two
#
# Пример ответа:
#
# Twenty one
# Twenty two


fin = open('input_w06e03.txt', 'r', encoding='utf8')
fout = open('output_w06e03.txt', 'w', encoding='utf8')

s = fin.read()
arr_s = s.split()

word_count = {}

for word in arr_s:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

count_word = {}
for key, value in word_count.items():
    if value in count_word:
        count_word[value].append(key)
    else:
        count_word[value] = [key]

sorted_count_word = sorted(count_word, reverse=True)
for i in sorted_count_word:
    print(*sorted(count_word[i]), end=" ", file=fout)

fin.close()
fout.close()