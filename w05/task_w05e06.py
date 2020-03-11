# Во входной строке записана последовательность чисел через пробел. Для
# каждого числа выведите слово YES (в отдельной строке), если это число ранее
# встречалось в последовательности или NO, если не встречалось.
#
# Sample Input:
#
# 1 2 3 2 3 4

# Sample Output:
#
# NO
# NO
# NO
# YES
# YES
# NO

original_list = list(map(int, input().split()))

myset = set()

for n in original_list:
    if n in myset:
        print('YES')
    else:
        print('NO')
    myset.add(n)
