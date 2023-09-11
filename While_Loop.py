# ---While Loop---

# Цикл While будет выполняться и повторять код до тех пор пока указанное условие True
# Важно убедиться что в конечом итоге цикл придет к Faulse, чтобы избежать бесконечного его выполнения

import random
i = 10
while i < 50:  # Условие цикла
    print(i)
    i += 10  # Необходимо изменять значение переменной которая влияет на условие внутри цикла
'''
while True:
    answer = input('Do you want to continue?: ')
    if answer == 'no':  # При выполнения условия цикл прерывается
        break  # Cпособ принудительного прирывания цикла

'''
'''
random_num = random.randint(1, 5)

while True:
    user_number = int(input('Try to huess number: '))
    if user_number != random_num:
        print('Try again')
        continue
    print('Congratilation!', random_num)
    break
'''

# --- Practice Task ---
while True:
    try:
        number_one = float(input('Enter first number: '))
        number_two = float(input('Enter second number: '))
    except ValueError as e:
        print(e)
        print('You have to enter numbers!')
        continue
    except ZeroDivisionError as e:
        print(e)
        print('Cannot devide by 0. Please enter a non-zero number')
        continue

    devision_nums_result = float(number_one / number_two)
    print(devision_nums_result)

    question_to_continue = input('Do you want to continue? Yes/No: ')
    if question_to_continue.lower() != 'yes':
        break
