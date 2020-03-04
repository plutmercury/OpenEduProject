# В списке все элементы различны. Поменяйте местами минимальный и максимальный
# элемент этого списка.
#
# Sample Input:
#
# 3 4 5 2 1
#
# Sample Output:
#
# 3 4 1 2 5


#arr = list(map(int, input().split()))

arr = [1, 2, 3, 4, 5]

max = arr[0]
max_pos = 0

min = arr[0]
min_pos = 0

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        max_pos = i
    elif arr[i] < min:
        min = arr[i]
        min_pos = i

arr[max_pos], arr[min_pos] = arr[min_pos], arr[max_pos]

print(*arr)
