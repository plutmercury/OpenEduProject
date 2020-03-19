fin = open('test.csv', 'r', encoding='utf8')

vals = []

for line in fin:
    now = line.split(',')
    vals.extend(list(map(int, now)))

vals.sort()
print(vals[len(vals) // 2], sum(vals) / len(vals))

fin.close()
