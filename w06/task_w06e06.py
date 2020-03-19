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


fin = open('input_w06e06.txt', 'r', encoding='utf8')

lines = fin.readlines()

counter_lines = {}

for l in lines:
    llen = len(l)
    if llen in counter_lines:
        counter_lines[llen].append(l)
    else:
        counter_lines[llen] = [l]

max_length = sorted(counter_lines, reverse=True)[0]

for l in sorted(counter_lines[max_length]):
    print(l)
