# --- Тернарный оператор в Python ---

# Это оператор позволяющий выразить условие и в зависимсоти от его выполнения вернуть разные значение

x = 10

message = 'number more than 5' if x > 5 else 'number less than 5'
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [x for x in numbers if x %
                2 == 0]  # Примпенение в List Comprehension
print(even_numbers)

tempt = 24
weather = 'hot' if tempt > 18 else 'cold'
print(weather)

my_img = ('1920', '1080')
info = f'{my_img[0]}x{my_img[1]}' if len(
    my_img) == 2 else 'Incorrect image formatting'

leng_info = 'string is long' if len(info) > 79 else 'string is short'
