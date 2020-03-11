# В первой строке задаётся количество названий столиц и государств - число N.
# В следующих N строках задаются названия столиц и государств по одному в
# строке, слова разделяются одним пробелом. Отсортируйте названия столиц и
# государств по названию государства в алфавитном порядке и выведите их по
# одному в строке.
#
# Sample Input:
#
# 2
# Moscow Russia
# Vienna Austria
#
# Sample Output:
#
# Vienna Austria
# Moscow Russia


def country(x):
    return x[1]


lst = []

N = int(input())

for i in range(N):
    lst.append(tuple(input().split()))

sortedlst = sorted(lst, key=country)

for s in sortedlst:
    print(*s)

