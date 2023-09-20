given_number = int(input('Write the number: '))
numbers = {}

for n in range(1, given_number + 1):
    numbers[n] = n * n

print(numbers)
