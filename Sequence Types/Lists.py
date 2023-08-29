# --- РАБОТА СО СПИСКАМИ. List ---

# Элементы в списке упорядочены и имеют свои индексы, по которым можно обращаться
# Список может содержать элементы разных типов, а так же одинаковые значения
# Список можно изменять (добаление, удаление, изменение элемента)

customers = ['Bob', 'John', 'Sian']

customers.remove('Sian')
print(customers)
removed_el = customers.pop(0)  # присвоение удаленного значения переменной
print(removed_el)

index = [251, 574, 10, 1]  # сортировка списка
index.sort(reverse=False)

greeting = 'Hello frm Python'
greet_letters = list(greeting)  # преобразование строки в список


ratings = [2.3, 3, 4, 7, 8]

print(max(ratings))  # манипуляции со списком
print(sum(ratings))
print(sum(ratings) / len(ratings))
all_numbers = index + ratings  # обьединение списков

# cсоздание копии списка. копирование метод Слайс(Вариант 1)
copied_ratings = ratings[:]
copied_ratings.append('228')  # добавления значения в список
print(copied_ratings)

copied_ratings2 = ratings.copy()  # использование метода Copy
copied_ratings2.append('188')
print(id(ratings) == id(copied_ratings2))  # проверка на сходство


# практика

nums = [10, 50, 0, 5, 100]
nums.insert(2, -5)  # метод добавления в список
# nums.clear() очищает список
# nums.extend('abc') добавление в списк элементов
other_nums = nums.copy()
other_nums.append(228)

print(nums.count(5)) # считает колво. указаных значений


list2 = [2, 3]
list1 =+ list2
print(list1)

# Task 2
list1 = list1.__add__(list2)
list1.extend(list2)
print(list1)
