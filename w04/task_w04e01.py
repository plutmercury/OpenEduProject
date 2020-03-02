# Вводится целое положительное число N. Выведите все числа по убыванию
# от N до 1 включительно через пробел.
#
# Sample Input:
#
# 8
#
# Sample Output:
#
# 8 7 6 5 4 3 2 1

N = int(input())

for i in range(N, 0, -1):
    print(i, end=' ')
