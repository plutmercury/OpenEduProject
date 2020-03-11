# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно
# как в первом списке, так и во втором.
#
# Sample Input:
#
# 1 3 2
# 4 3 2
#
# Sample Output:
#
# 2

set_one = set(map(int, input().split()))
set_two = set(map(int, input().split()))

c = 0
for i in set_one:
    if i in set_two:
        c += 1

print(c)
