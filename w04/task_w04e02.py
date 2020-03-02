# Вводится число целое положительное число N. Напечатайте все N-значные
# нечетные целые положительные числа в порядке убывания. Например, если
# вводится число 3, то необходимо печать трёхзначные числа (состоящие из
# трех цифр).
#
# Подсказка: Вспомните про возведение 10 в степень.
#
# Sample Input:
#
# 1
#
# Sample Output:
#
# 9 7 5 3 1

N = int(input())

for i in range(10**N-1, 10**(N-1)-1, -2):
    print(i, end=' ')
