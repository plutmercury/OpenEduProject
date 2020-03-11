# В первой строке задаётся количество названий столиц - число N. В следующих
# N строках задаются названия столиц по одному в строке. Отсортируйте названия
# столиц в алфавитном порядке и выведите их по одному в строке.
#
# Sample Input:
#
# 2
# Moscow
# Berlin
#
# Sample Output:
#
# Berlin
# Moscow

lst = []
N = int(input())
for i in range(N):
    lst.append(input())

lst.sort()

for s in lst:
    print(s)

