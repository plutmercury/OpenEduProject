A = int(input())
B = int(input())

M = A * 60 + B

H = M // 60 % 24
M = M % 60

print(H, M)