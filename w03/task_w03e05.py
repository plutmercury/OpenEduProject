P = abs(int(input())) # процентов годовых
X = abs(int(input())) # рублей
Y = abs(int(input())) # копеек


def interest(x, y, i):
    s = (x + y / 100) * (100 + i)
    return int(s // 100), int(s % 100)


x1, y1 = interest(X, Y, P)
print(x1, y1)

# Сравнение с альтернативным решением
#def print_interest2(x, y, i):
#    s = (x * 100 + y) * (1 + i / 100)
#    return int(s // 100), int(s % 100)
#
#
#for i in range(0, 101):
#    for j in range(0, 1000):
#        for p in range(1, 13):
#            x1, y1 = print_interest1(j, i, p)
#            x2, y2 = print_interest2(j, i, p)
#            if (x1 != x2) or (y1 != y2):
#                print(j, i, p, ":", x1, y1, end="; ")
#                print(j, i, p, ":", x2, y2)


