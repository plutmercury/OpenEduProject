# В введенной строке необходимо заменить все буквы A на B, а все
# буквы B - на A. Заменять нужно только заглавные буквы.
#
# Sample Input:
#
# ABABAC
#
# Sample Output:
#
# BABABC

s = input()

s = s.replace('A', '#')
s = s.replace('B', 'A')
s = s.replace('#', 'B')

print(s)