# Напишите программу, которая считывает два целых числа A и B и выводит
# наибольшее значение из них. Числа — целые от 1 до 1000.
#
# Sample Input:
#
# 8
# 5
#
# Sample Output:
#
# 8

A = int(input())
B = int(input())
if A >= B:
    print(A)
else:
    print(B)
