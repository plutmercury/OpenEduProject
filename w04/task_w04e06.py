# В первой строке вводится строка-разделитель.
#
# Во второй строке вводится текст, состоящий из слов, разделенных пробелом.
#
# Выведите слова из текста, разделяя их строкой-разделителем.
#
# Sample Input:
#
# 123
# A B Cd Efg
#
# Sample Output:
#
# A123B123Cd123Efg

sep = str(input())
s = str(input())
print(sep.join(s.split()))
