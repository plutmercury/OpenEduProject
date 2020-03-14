"""
3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa
"""


def parse(s):
    eng_w = s[:s.find(' - ')]
    latins = s[s.find(' - ') + 3:].split(', ')
    return eng_w, latins


N = int(input())
lat_eng = {}

for _ in range(N):
    s = input()
    eng_w, latins = parse(s)
    for lat_w in latins:
        if not lat_w in lat_eng:
            lat_eng[lat_w] = []
        lat_eng[lat_w].append(eng_w)

print(len(lat_eng))
for lat_w in sorted(lat_eng):
    print(lat_w, end=' - ')
    print(', '.join(sorted(lat_eng[lat_w])))

