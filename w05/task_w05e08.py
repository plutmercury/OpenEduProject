# Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
# языки знают все школьники и языки, которые знает хотя бы один из школьников.
#
# Первая строка входных данных содержит количество школьников N. Далее идет N
# чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков,
# которые знает i-й школьник.
#
# В первой строке выведите количество языков, которые знают все школьники.
# Начиная со второй строки - список таких языков, упорядоченный по алфавиту.
# Затем - количество языков, которые знает хотя бы один школьник, на следующих
# строках - список таких языков, упорядоченный по алфавиту.
#
# Sample Input:
#
# 3
# 3
# Russian
# English
# Japanese
# 2
# Russian
# English
# 1
# English
#
# Sample Output:
#
# 1
# English
# 3
# English
# Japanese
# Russian

N = int(input())  # количество школьников

M = []  # количество языков, которые знает каждый школьник
for i in range(N):
    M.append(set())
    Mi = int(input())
    for _ in range(Mi):
        M[i].add(input())

#M = [{'Japanese', 'Russian', 'English'}, {'Russian', 'English'}, {'English'}]

allsb = None
atleastsb = None
for sb in M:
    if allsb is None or atleastsb is None:
        allsb = sb
        atleastsb = sb
    allsb = allsb & sb
    atleastsb = atleastsb | sb

print(len(allsb))
for language in sorted(allsb):
    print(language)
print(len(atleastsb))
for language in sorted(atleastsb):
    print(language)
