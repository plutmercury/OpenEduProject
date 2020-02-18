N = int(input())
counter_zeroes = 0

while N > 0:
    number = int(input())
    N -= 1
    if number == 0:
        counter_zeroes += 1

print(counter_zeroes)