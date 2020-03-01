# В введенной строке необходимо заменить все буквы A на B, а все буквы C - на D.
# Заменять нужно только заглавные буквы.
#
# Sample Input:
#
# ABCDabcdABCD
#
# Sample Output:
#
# BBDDabcdBBDD

s = input()

s = s.replace('A', 'B')
s = s.replace('C', 'D')

print(s)