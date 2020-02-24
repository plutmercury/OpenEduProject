P = abs(int(input())) # процентов годовых
X = abs(int(input())) # рублей
Y = abs(int(input())) # копеек


def print_interest(x, y, i):

    s = x *100 + y
    s *= 1 + i / 100
    print(int(s / 100), round(s - int(s / 100) * 100))
    return 0


def rround(x):
    if (x - int(x)) < 0.5:
        return int(x)
    else:
        return int(x) + 1


print_interest(X, Y, P)

print_interest(179, 0, 12)
print_interest(1000, 0, 12)
