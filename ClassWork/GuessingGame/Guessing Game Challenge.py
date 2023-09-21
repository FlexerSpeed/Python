import random

random_num = random.randint(1, 100)
previus_difference = None

while True:
    user_number = input('Please enter your guess from 1 to 100: ')

    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print('You need enter a numeric type!' + '\n' + ('_' * 30))
        continue

    if user_number < 1 or user_number > 100:
        print('You need enter a number in valid range!' + '\n' + ('_' * 40))
        continue

    difference = abs(random_num - user_number)

    if previus_difference is None:
        if (difference <= 10):
            message = 'Warm!'
            previus_difference = difference
        else:
            message = 'Cold'

    if previus_difference is not None and difference != 0:
        if (previus_difference > difference and difference < 5):
            message = 'HOT!'
        elif (previus_difference < difference):
            message = 'Colder'
        elif (previus_difference > difference):
            message = 'Warmer!'
    print(message + '\n' + ('~' * 7))

    if user_number == random_num:
        print('Congratulations!' + '\n' + ('*' * 16))
        break
