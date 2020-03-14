# Даны два списка чисел. Выведите все числа, которые входят как в первый, так
# и во второй список в порядке возрастания.
#
# Sample Input:
#
# 1 3 2
# 4 3 2
#
# Sample Output:
#
# 2 3

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

set3 = sorted(set1 & set2)

print(*set3)


