number = int(input())
counter = 1
maximal_number = number

while number != 0:
    number = int(input())
    if number == maximal_number:
        counter += 1
    elif number > maximal_number:
        counter = 1
        maximal_number = number

print(counter)