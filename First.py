

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

# print(my_motorbike['price'])
my_motorbike['price'] = 7000  # изменение значений
my_motorbike['is_new'] = True  # добавление элементов
# del my_motorbike['engine_vol']  # удаление ключа из словаря

key_name = 'brand'  # присвоение ключа переменной
my_motorbike[key_name] = 'BMW'
# print(len(my_motorbike)) #получение колва клбчей в словаре
# print(my_motorbike.get('model', 1))  # предпочтительный метод запроса к ключам. (1) знаение на случай отсуцтвия ключа

my_disk = {}

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

new_disk = my_disk.copy()  # копирование и создание нового словаря
new_disk['type'] = 'ssd'

# при конвертации листа в словарь значения должны быть представлены в кортеже (ключ, значение)
my_list = [('model', 'Samsung'), ('Availeble', True)]
my_dic = dict(my_list)

print(my_dic)
