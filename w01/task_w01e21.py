A = int(input()) # ширина комнаты
B = int(input()) # длина комнаты
D = int(input()) # длина куска рулона
C = 1 # ширина куска рулона

roomArea = A * B
rollArea = C * D

print((roomArea - 1) // rollArea + 1)
