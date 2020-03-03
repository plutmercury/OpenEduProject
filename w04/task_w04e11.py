# Дан список чисел. Определите, сколько в этом списке элементов, которые
# больше двух своих соседей и выведите количество таких элементов.
#
# Sample Input:
#
# 1 5 1 5 1
# Sample Output:
#
# 2

s = str(input())
a = list(map(int, s.split()))
r = 0

for i in range(len(a)):
    if i > 0 and i < len(a) - 1:
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            r += 1

print(r)



