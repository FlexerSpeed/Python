# --- Словари в пайтон. Dictionary ---

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

my_motorbike['price'] = 7000  # изменение значений
my_motorbike['is_new'] = True  # добавление элементов
# del my_motorbike['engine_vol']  # удаление ключа из словаря

key_name_for_dic = 'brand'  # присвоение ключа переменной
my_motorbike[key_name_for_dic] = 'BMW'
# print(len(my_motorbike)) #получение колва клбчей в словаре
# print(my_motorbike.get('model', 1))  # предпочтительный метод запроса к ключам. (1) знаение на случай отсуцтвия ключа

my_disk = {}

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

new_disk = my_disk.copy()  # копирование и создание нового словаря
new_disk['type'] = 'ssd'

# Обьединение словарей при помощи |
union_dic = my_motorbike | my_disk

# при конвертации листа в словарь значения должны быть представлены в кортеже (ключ, значение)
my_list = [('model', 'Samsung'), ('Availeble', True)]
my_dic = dict(my_list)

print(my_dic)


# ---Practical Task---  (переделать при помощи циклов)
inputs = {}

key1 = input('Input key: ')
value1 = input('Input value: ')
inputs[key1] = value1

key2 = input('Input key: ')
value2 = input('Input value: ')
inputs[key2] = value2

key3 = input('Input key: ')
value3 = input('Input value: ')
inputs[key3] = value3

print(inputs)

# ---Practical Task 2---
team_one = {
    'mannager 1': 'Paul Dune',
    'sale assistant 2': 'Eduard Tern',
    'stockroomer': 'Andre Bill'
}

team_two = {
    'mannager 2': 'Kevin McLaughlin',
    'sale assistant 2': 'Joe Hot',
    'stockroomer': 'Andre Bill'
}

team_tre = {
    'manager 3': 'Eddy Boy',
    'sale assistant 3': 'Imran Indi',
    'stockroomer': 'Andre Bill'
}
total_emploees = team_one | team_two| team_tre
print(total_emploees)