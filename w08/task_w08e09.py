# Напишите программу, которая будет разрезать большую прямоугольную область на
# N×N одинаковых прямоугольных областей. Области задаются четырьмя координатами:
# минимальной широтой, минимальной долготой, максимальной широтой, максимальной
# долготой.
#
# При выводе области должны быть упорядочены по возрастанию минимальной широты,
# а в случае равных широт - по возрастанию минимальной долготы.
#
# Гарантируется, что все числа во входных данных положительны.
#
# Sample Input:
#
# 41.173 77.23 42.17 79.004
# 2
#
# Sample Output:
#
# 41.173 77.23 41.6715 78.117
# 41.173 78.117 41.6715 79.004
# 41.6715 77.23 42.17 78.117
# 41.6715 78.117 42.17 79.004

rect = list(map(float, input().split()))
N = int(input())

dlat = (rect[2] - rect[0]) / N
dlon = (rect[3] - rect[1]) / N

for i in range(N):
    for j in range(N):
        print(rect[0] + dlat * i, rect[1] + dlon * j, rect[0] + dlat * (i + 1), rect[1] + dlon * (j + 1))



