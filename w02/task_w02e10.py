# Даны три целых числа. Найдите наибольшее из них (программа должна вывести
# ровно одно целое число).
#
# Sample Input:
#
# 1
# 2
# 3
#
# Sample Output:
#
# 3

number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 >= number2:
    if number1 >= number3:
        print(number1)
    else:
        print(number3)
elif number2 >= number3:
    print(number2)
else:
    print(number3)
