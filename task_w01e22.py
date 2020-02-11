A = int(input()) # ширина комнаты
B = int(input()) # длина комнаты
C = int(input()) # height of the wall
D = int(input()) # length of the roll
E = 1 # width of the roll

wallArea = 2 * C * (A + B )
rollArea = D * E

print((wallArea - 1) // rollArea + 1)