# --- Functions ---

# Функция это блок кода который можно выполнять многократно
# Функция это обьект как и всё в Python и вкдёт себя как обьект
# Функция всегда возвращает значение
# Не рекомендуется в функции изменять внешние переменные и обьекты

a = 5
b = 3
c = a + b

#1) ключ.слово.def 2) имя функ. 3) параметры
def sum (a,b): # параметры = переменные, имеют локальную область видимости (Scope)
    a = a + 1  # параметы можно изменять внутри функции
    c = (a + b) / 2  # Тело функции
    return c   # Возврат результата


res = sum(5, 3) # аргументы (параметры) определяются при вызове функции
print(res)

#Правильная работа в функции с внешними переменными
def increase_person_age(person, name):
    person_copy = person.copy() # Важно создать копию обьекта, для того чтобы он не изменялся
    person_copy['age'] += 1
    person_copy['name'] = name     # Если обьект имеет внутренние ссылки нужно использовать метод Deepcopy
    return person_copy


person_one = {
    'name': 'Michael',
    'age': 31
}

new_person = increase_person_age(person_one, 'John') # Создаем новый обьект при помощи функции 
print(new_person)
print(person_one)

# --- Practical Task ---
def merge_list_to_dict (list1, list2):
    return dict(zip(list1, list2))


products = ['TV', 'iron', 'hower', 'frizor']
prices = [1200, 50, 90, 900]
invoice = merge_list_to_dict(products, prices)
print(invoice)