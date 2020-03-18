# Выведите все строки данного входного файла в обратном порядке. Для этого
# считайте список всех строк при помощи метода readlines().
#
# Последняя строка входного файла заканчивается символом '\n'.
#
# Ссылка на входной файл:
# https://stepik.org/media/attachments/lesson/258918/input.txt

fin = open('input_w06e04.txt', 'r', encoding='utf8')

s_arr = fin.readlines()

for s in s_arr[::-1]:
    print(s, end='')
