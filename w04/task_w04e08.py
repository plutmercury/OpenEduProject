# Выведите все четные элементы списка.
#
# Sample Input:
#
# 1 2 2 3 3 3 4
#
# Sample Output:
#
# 2 2 4

a = list(map(int, str(input()).split()))
for i in a:
    if i % 2 == 0:
        print(i, end=' ')
