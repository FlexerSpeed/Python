import math

input_numbers = input('Please enter tree numbers: ')

numbers = input_numbers.split(',')
results = []

for i in numbers:
    i = int(i)
    result = int(math.sqrt((2 * 50 * i) / 30))
    results.append(result)

print(', '.join(map(str, results)))
