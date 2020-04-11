# Даны три целых числа A, B, C. Выведите YES, есть ли среди них хотя бы одно
# четное и хотя бы одно нечетное, и NO в противном случае.
#
# Sample Input:
#
# 3
# 4
# 5
#
# Sample Output:
#
# YES

A = int(input())
B = int(input())
C = int(input())

if ((A % 2 == 0) or (B % 2 == 0) or (C % 2 == 0)) and ((A % 2 != 0) or (B % 2 != 0) or (C % 2 != 0)):
    print('YES')
else:
    print('NO')
