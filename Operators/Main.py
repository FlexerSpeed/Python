# --- Operators ---

# Арифметические  + - * /
# Операторы сравнения == != < >
# Логические операторы not and or
# Оператор присовения =
# is (оператор проверки совпадений) is not  in  not in

# Унарные операторы всегда имеют один операнд )(-, ~, not)
# Бинарные операторы имеют два оперенда (=, +, +=, ==, and)

# Пример использования in, not in
my_car = {
    'brand': 'BMW',
    'prise': 15000
}

print('brand' in my_car) #проверка на наличие ключа
print('value' not in my_car) #проверка на отсутствие ключа

# ---Приоритетность операторов---
# по порядку: (), унарные оп., арифметические опер., опер. сравнения, логические опер., опер. присваивания


# ---Practical Task---
set1 = {2, 5, 50, 100}
set2 = {2, 5, 50, 100}

print(set1 == set2)
print(set1 is set2)
print(50 in set2)

# ---Лгические оператры---
# AND и OR (short-circuit) операторы короткого замыкания

# ---Practical Task---

dict_one = {
    'brand': 'BMW',
    'prise': 15000
}

dict_two = {
    'brand': 'BMW',
    'prise': 14000
}

def dict_equel (dict1, dict2):
    if dict1 and dict2 == True:
        print('Dictinores are equel')
    else:
        print('Dictiones are not equel')

dict_equel(dict_one, dict_two)

#---Оператор для разделения словаря---
# Оператор распковки словаря в другой словарь - **

button = {
    'width': 200, # словарь1 со значениями
    'text': 'Buy'
}

red_button = {
    **button, # распаковка значений словаря1 в новый словарь при помощи оператора **
    'color': 'red'
}
print(red_button)

# Так же при помощи оператора ** можно обьеденять два словаря
new_button = {
    **button
    **red_button
}



