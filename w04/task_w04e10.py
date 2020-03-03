# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента.
#
# Sample Input:
#
# 1 5 2 4 3
#
# Sample Output:
#
# 5 4

s = str(input())
a = list(map(int, s.split()))
r = []

for i in range(len(a)):
    if i > 0:
        if a[i] > a[i - 1]:
            r.append(a[i])

print(*r)



