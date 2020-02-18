maximumNumber = 0
number = int(input())

while number != 0:
    if number > maximumNumber:
        maximumNumber = number
    number = int(input())

print(maximumNumber)
