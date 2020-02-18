number = int(input())
counter = 0

while number != 0:
    prev_number = number
    number = int(input())
    if number > prev_number:
        counter += 1

print(counter)
