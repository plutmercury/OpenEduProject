# Дана строка. Выведите слово, которое в этой строке встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом
# (алфавитном) порядке.
#
# Sample Input:
#
# apple orange banana banana orange
#
# Sample Output:
#
# banana

words = input().split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

count_word = {}
for word in word_count:
    if word_count[word] in count_word:
        count_word[word_count[word]].append(word)
    else:
        count_word[word_count[word]] = [word]

sorted_count_word = sorted(count_word, reverse=True)
print(sorted(count_word[sorted_count_word[0]])[0])
