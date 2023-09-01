# --- Using Arguments in Tuple ---
# * - обьединение аргументов в кортеж

def sum_nums(*args): # указание обьединения параметров в кортеж
    print(args)
    print(args[0])
    return sum(args) # Возврат сумы кортежа


# --- Обьединение аргументов в словарь
# ** - Обьединяет аргументы в словарь
print(sum_nums(2, 3, 7)) # Передача кортежа в аргумент

def get_post_info(**person):
    info = (
        f"{person['name']} wrote " # f-strings (f строки) позволяет вставлять переменные в строку
        f"{person['post_id']} posts"
    )
    return info

info = get_post_info(name='Michael', post_id=278)
print(info)

def get_newpost_info(name, post_id): # Иcпользование аргументов с ключевыми словами
    info = f"{name} wrote {post_id} posts" 
    return info

new_info = get_post_info(name='Michael', post_id=278)
print(new_info)


# --- Значение аргументов по умолчанию ---
# Аргументы по умолчанию становятся не обязательными. Если его не передать исп. значение по умолчанию
# Значенниями этих аргум. могут быть обьекты любого типа данных
# Значения по умолчанию должны следоваь после обязательгых параметров в сигнатуре функции

from datetime import date # datatime стандартный модуль Python предост. классы и функц. для работы с временем и датой
# класс date испоьзуется только для работы с датой (без времени)
# класс date позволяет работать напрямую без написания datetime.data без написания каждый раз для использования
def get_date():
    return date.today().strftime('%A') 
print(get_date())

def create_new_post (post, week_day=get_date()): # установление функции как параментр по умолчанию
    copy_of_post = post.copy() # копируем внешний изменяемый обьект!!!
    copy_of_post['day_of_creation'] = week_day
    return copy_of_post

init_post = {
    'user': 'Mchaele',
    'age': 31
}

new_post = create_new_post(init_post) # Использование аргумента по умолчанию
print(new_post)
new_post2 = create_new_post(init_post, week_day='Wednesday') # использование аргумента с ключевым словом
print(new_post2)


# --- Practical Task ---
def merge_list_to_dict (list1, list2):
    return dict(zip(list1, list2))


products = ['TV', 'iron', 'hower', 'frizor']
prices = [1200, 50, 90, 900]
invoice = merge_list_to_dict(list1=products, list2=prices) # Использование аргументов с ключ. словами
print(invoice)

invoice2 = merge_list_to_dict(['TV', 'hower', 'iron'], list2=prices) # 1 аргумент позиционный, 2 ключ. слово
print(invoice2)

# --- Task 2 ---
def update_car_info(**car): # Создание словаря через команду **
    car ['is_availeble'] = True 
    return car

print(update_car_info(brand='BMW', price=10000)) #Передача ключ значение в словарь функции

# --- Task 3 ---
# F strings
person = "John"
employee = True
sallary = 3500
family = ['wife', 'son', 'daughter']

print(f'{person} has a job ({employee}) and hi has {sallary} per mounths. John family are {family}')
