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

    