# Выведите в обратном порядке содержимое всего файла полностью. Для этого
# считайте файл целиком при помощи метода read().
#
# Ссылка на входной файл:
# https://stepik.org/media/attachments/lesson/258921/input.txt
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
# .detacilpmoc naht retteb si xelpmoC
# .xelpmoc naht retteb si elpmiS
# .ticilpmi naht retteb si ticilpxE
# .ylgu naht retteb si lufituaeB

fin = open('input_w06e07.txt', 'r', encoding='utf8')
fout = open('output_w06e07.txt', 'w', encoding='utf8')

t = fin.read().strip()

print(t[::-1], file=fout)

fin.close()
fout.close()
