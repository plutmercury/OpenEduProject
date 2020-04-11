# Даны два целых числа. Программа должна вывести число 1, если первое число
# больше второго, число 2, если второе больше первого или число 0, если они
# равны.
#
# Эту задачу нужно решить с помощью конструкций if-elif
#
# Sample Input:
#
# 1
# 2
#
# Sample Output:
#
# 2

number1 = int(input())
number2 = int(input())

if number1 > number2:
    print(1)
elif number2 > number1:
    print(2)
else:
    print(0)
