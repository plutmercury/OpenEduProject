# В csv-файле (разделитель - точка с запятой, кавычки не используются)
# содержится анонимизированная информация о зарплатах сотрудников в различных
# компаниях. В первом столбце записано название компании, а во втором -
# зарплата. Упорядочите компании по возрастанию средней зарплаты. В случае
# одинаковых средних зарплат в нескольких компаниях их следует упорядочить по
# алфавиту.
# Названия компаний следует выводить по одному в строке.
#
# Совет: используйте словарь, где ключом будет служить название компании, а в
# качестве значения будет храниться суммарная зарплата и количество
# сотрудников.
#
# csv-файл доступен по ссылке:
# https://stepik.org/media/attachments/lesson/258922/input.csv

fin = open('input_w06e08.csv', 'r', encoding='utf8')

dict = {}

for line in fin:
    com_sal = line.split(';')
    if com_sal[0] in dict:
        dict[com_sal[0]][0] += int(com_sal[1])
        dict[com_sal[0]][1] += 1
    else:
        dict[com_sal[0]] = [int(com_sal[1])]
        dict[com_sal[0]].append(1)

fin.close()

averages = {}
for company_name, company_values in dict.items():
    average = company_values[0]/company_values[1]
    if average in averages:
        averages[average].append(company_name)
    else:
        averages[average] = [company_name]

for average, companies in sorted(averages.items()):
    for company in sorted(companies):
        print(company)
