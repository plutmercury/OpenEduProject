# В этой задаче вам необходимо научиться генерировать html-код на питоне и
# сдать на проверку html-файл, в котором будет таблица размером 10 на 10,
# которая должна содержать таблицу умножения для чисел от 1 до 10. При открытии
# вашего файла в браузере это должно выглядеть примерно так:
#   1 2
#   3 4
# Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и
# </html>.
#
# Для создания таблицы можно пользоваться тегами <table> (создание таблицы),
# <tr> (создание строки в таблице) и <td> (создание отдельной ячейки). Все
# открытые теги нужно закрыть, причем сделать это нужно в правильном порядке.
#
# Пожалуйста, не используйте никаких украшений и других тегов - мы не сможем
# проверить такие решения.


fout = open('output_w07e02.html', mode='w')

print('<html>', '<body>', '<table>', sep='\n', file=fout)
for i in range(1, 11):
    print('<tr>', end='', file=fout)
    for j in range(1, 11):
        print('<td>', i*j, '</td>', sep='', end='', file=fout)
    print('</tr>', file=fout)
print('</table>', '</body>', '</html>', sep='\n', file=fout)

fout.close()