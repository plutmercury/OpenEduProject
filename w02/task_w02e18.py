# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это
# количество.
#
# Формат ввода
# Cначала вводится число N, затем вводится ровно N целых чисел.
#
# Формат вывода
# Выведите ответ на задачу.
#
# Sample Input:
#
# 5
# 0
# 7
# 0
# 2
# 2
#
# Sample Output:
#
# 2

N = int(input())
counter_zeroes = 0

while N > 0:
    number = int(input())
    N -= 1
    if number == 0:
        counter_zeroes += 1

print(counter_zeroes)