# --- РАБОТА СО СПИСКАМИ. List ---

# Элементы в списке упорядочены и имеют свои индексы, по которым можно обращаться
# Список может содержать элементы разных типов, а так же одинаковые значения
# Список можно изменять (добаление, удаление, изменение элемента)

customers = ['Bob', 'John', 'Sian']

customers.remove('Sian')
print(customers)

index = [251, 574, 10, 1]  # Сортировка списка
index.sort(reverse=False)
index.reverse()  # Метод который переворачивает список (индексы элементов меняются)

greeting = 'Hello frm Python'
greet_letters = list(greeting)  # Преобразование строки в список


ratings = [2.3, 3, 4, 7, 8]

# Манипуляции со списком
print(max(ratings))
print(sum(ratings))
print(sum(ratings) / len(ratings))

all_numbers = index + ratings  # Обьединение списков

# Создание копии списка
copied_ratings = ratings[:]  # Копирование метод Слайс(Вариант 1)
copied_ratings2 = ratings.copy()  # Использование метода Copy (Вариант 2)

# Добавление - удаление элементов в лист
ratings = ratings + ['abc', 'fgh']  # Добавление в список значений
ratings.append('228')  # Добавления значения в список
# Удаление элемента по индексу (следуюший элемент преобретает индекс удаленного)
ratings.pop(0)
# Метод pop имеет ДЕФОЛТНЫЙ параметр индекса (-1) (удаляет последний элемент листа)
removed_el = ratings.pop(0)  # Присвоение удаленного значения переменной
print(ratings, end='')

print(id(ratings) == id(copied_ratings2))  # Проверка на сходство

# MATRIX
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e', 'f']
matrix = [lst1, lst2]  # матрица это обьединение списков в список
print(matrix[1])  # обращаясь к элементу в матрице мы получаем целый список

# Практика
nums = [10, 50, 0, 5, 100]
nums.insert(2, -5)  # метод добавления в список
# nums.clear() очищает список
# nums.extend('abc') добавление в списк элементов
other_nums = nums.copy()
other_nums.append(228)

print(nums.count(5))  # считает колво. указаных значений


list2 = [2, 3]
list1 = list2
print(list1)

# Task 2
list1 = list1.__add__(list2)
list1.extend(list2)
print(list1)


a = []
a.append(1, 2, 3, 4)
print(a[1])
