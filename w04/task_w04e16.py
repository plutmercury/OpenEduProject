# Напишите функцию sort3, которая принимает 3 параметра a, b, c, переставляет
# их так чтобы и возвращает тройку чисел a, b, c.
#
# Дано три числа по одному в строке. Воспользуйтесь функцией sort3 чтобы
# упорядочить эти три числа.
#
# Sample Input:
#
# 1
# 2
# 1
#
# Sample Output:
#
# 1 1 2


def sort3(a, b, c):
    if b <= a <= c:
        return b, a, c
    elif b <= c <= a:
        return b, c, a
    elif a <= c <= b:
        return a, c, b
    elif c <= a <= b:
        return c, a, b
    elif c <= b <= a:
        return c, b, a
    return a, b, c


x = int(input())
y = int(input())
z = int(input())

print(*sort3(x, y, z))


