# На вход подается строка. Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов
# или символами конца строки. Для каждого слова из этого текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.
#
# Sample Input:
#
# one two one tho three
#
# Sample Output:
#
# 0 0 1 0 0

words = input().split()

unique_words = {}
counter = []

for word in words:
    if word in unique_words:
        unique_words[word] += 1
    else:
        unique_words[word] = 0
    counter.append(unique_words[word])

print(*counter)
