# По введенному целому положительному числу N посчитайте N! (N факториал).
#
# Фавториалом числа N называется произведение всех чисел от 1 до N.
#
# Sample Input:
#
# 4
#
# Sample Output:
#
# 24

N = int(input())

r = 1
for i in range(1, N+1):
    r *= i

print(r)