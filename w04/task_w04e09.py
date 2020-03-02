# Дан список чисел. Выведите значение наибольшего элемента в списке, а затем
# индекс этого элемента в списке. Если наибольших элементов несколько,
# выведите индекс первого из них.
#
# Sample Input:
#
# 1 2 3 2 1
#
# Sample Output:
#
# 3 2

s = str(input())
a = list(map(int, s.split()))

biggest_n = None
biggest_i = None

for i in range(len(a)):
    if biggest_n is None or a[i] > biggest_n:
        biggest_n = a[i]
        biggest_i = i

print(biggest_n, biggest_i)
