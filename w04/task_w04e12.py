# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент, а значения
# всех элементов списка по модулю не превосходят 1000.
#
# Sample Input:
#
# 5 -4 3 -2 1
#
# Sample Output:
#
# 1

s = str(input())
a = list(map(int, s.split()))
r = 1000

for i in a:
    if i > 0 and i < r:
        r = i

print(r)
