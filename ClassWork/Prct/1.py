# --- Task one ---

numbers = range(2000, 3200)
list_numbers = []

for i in numbers:
    if (i % 7 == 0) and (i % 5 != 0):
        list_numbers.append(i)

print(list_numbers)
