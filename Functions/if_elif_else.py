# --- Statements ---

# if, if ... alse, if ... elif
# также существует тернарный оператор
# В ПАЙТОН ВСЕ ПУСТЫЕ ИЛИ = 0 ЗНАЧЕНИЯ = False

# --- IF ---
person_info = {
    'age': 20,
    'name': None
}
# Проверка на существование ключа 'name' и его значения
if not person_info.get('name'):
    print('The name is not exist')

num_one = 1
num_two = 2

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and  # Проверка на тип данных
        isinstance(num_two, int)):
    print('Both numbers are positive and int')


# --- ELSE ---
my_number = 21.5
# Оператор is используется для сравнения двух обьектов с точки зрения их идентичности (являются ли два обьекта одим и тем же обьектом)
if type(my_number) is int:  # Сравниваем тип данных
    print('number is integer')
else:
    print('number is not integer')


my_phone = {
    'price': 200,
    'brand': 'Apple'
}
if my_phone.get('brand'):  # Используем метод GET для проверки существ. ключа в словаре
    print('Brand is', my_phone['brand'])
else:
    print('Brand is not exist')


# --- ELIF ---
num_tree = -10

if num_tree > 0:
    print('number positive')
elif num_tree < 0:
    print('number negative')
else:
    print('number is 0')
