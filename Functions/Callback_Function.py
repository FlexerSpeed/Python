# --- CallBack Functions---

# Коллбэк функия это функция которая передаётся как аргумент в другой функции

def print_number_info (num): # КоллБэк функция
    if (num % 2) == 0:
        print('Entered number is even')
    else:
        print('Entered nuber is odd')

def print_square_num(num):
    print('Square of the num is', num * num)

def process_number(num, callback_fn): # Вызов коллбэк функции
    callback_fn(num)

#entered_number = int(input('Enter any number: '))
num = 2
#result = process_number(entered_number, print_number_info)
result = process_number(num, print_square_num)