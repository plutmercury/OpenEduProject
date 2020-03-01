# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме
# первого и последнего вхождения.
#
# Sample Input:
#
# In the hole in the ground there lived a hobbit
#
# Sample Output:
#
# In the Hole in tHe ground tHere lived a hobbit

s = input()

begin = s[:s.find('h') + 1]
middle = s[s.find('h') + 1:s.rfind('h')]
end = s[s.rfind('h'):]
middle = middle.replace('h', 'H')

print(begin + middle + end)
