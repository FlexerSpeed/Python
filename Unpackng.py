# --- Unpacking ---
# Извлеечние значений и присвоение значений переменным


# РАСПАКОВКА LIST
my_fruits_list = ['apple', 'banana', 'lime']
# Раскаковка из упордоченных обьктов происходят по индексам по порядку слева на право
# item(0)  item(1)   item(2)
my_apple, my_banana, my_lime = my_fruits_list
# Возможно распаковывать лист с сохранением его в новом листе при помощи
# item(0)  [item(1), item(2)]
my_apple, *remaining_fruits_list = my_fruits_list
# Распаковка листа в аргументы функции
details = ['V12', 2000]


def prise_dital(detail, prise=0):
    if not prise:
        return f'Print the {prise}'
    return f'The prise is {prise}$ for {detail}'


prise_dital(*details)  # Исполбзуем * для распаковки
# Передача из листа в именованные аргументы
prise_dital(prise=details[1], detail=details[0])
# Передача из листа в позиционные аргументы
prise_dital(details[0], details[1])


# РАСПАКОВКА TUPLE
my_fruits_tup = ('apple', 'banana', 'lime')
# Распаковка кортежей происходит так же
my_applet, my_bananat, my_limet = my_fruits_tup
# Возможно распаковывать кортеж с сохранением его в новом кортеже при помощи
my_applet, *remaining_fruits_tup = my_fruits_tup


# РАСПАКОВКА СЛОВАРЯ
user_profile = {
    'name': 'Michael',
    'age': 30
}


def user_info(name, age=0):
    if not age:
        return f'no {age} in parameters'
    return f'{name} has age {age}'


# Распаковываем словарь при помощи ** и передаем значения в параметры функции
user_info(**user_profile)
# Распаковки через передачу значений словаря в позиционные аргументы
user_info(user_profile['name'], user_profile['age'])
# Вариант с именованными аргументами
user_info(age=user_profile['age'], name=user_profile['name'])
