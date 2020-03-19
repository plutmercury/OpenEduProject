# В csv-файле (разделитель - точка с запятой, кавычки не используются)
# содержится анонимизированная информация о зарплатах сотрудников в различных
# компаниях. В первом столбце записано название компании, а во втором -
# зарплата.
#
# Поменяйте местами первый и второй столбцы, по-прежнему разделяя значения в
# ячейках одной строки точкой с запятой. Сохраняйте порядок строк.
#
# csv-файл доступен по ссылке:
# https://stepik.org/media/attachments/lesson/258922/input.csv

fin = open('input_w06e09.csv', 'r', encoding='utf8')
fout = open('output_w06e09.csv', 'w', encoding='utf8')

for line in fin:
    line_items = line.split(';')
    print(int(line_items[1]), line_items[0], sep=";",file=fout)

fout.close()
fin.close()