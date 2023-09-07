# --- ZIP functions---

# Позволяет обьеденять элементы из итерируемых обьктов, создавая кортежи по их нумерации
# В ZIP лучше обьеденять обьекты с упорядоченными элементами
# Если итераторы (обьединяемые обьекты) имеют разную длину, ZIP будет иметь длину самого короткого обьекта
# Может обьеденять разные типы обьектов (кортежи, листы)
# ZIP можно конвертировать в словарь только при обьединение 2х обьктов (потому что словарь = ключ: значение)

fruit = ['apple', 'banana', 'lime'] # список 1
quantities = (100, 70, 50) # кортеж 2

fruit_quan_zip = zip(fruit, quantities) # обьединение списка и кортежа при помощи ZIP
#              ('apple, 100'), ('banana', 70)...

fruit_quan_list = list(fruit_quan_zip) # конвертируем в лист для отображения значений в ZIP
print(fruit_quan_list)


# --- Practical Task ---
items = ['TV', 'iron', 'blender', 'frizor']
prises = [1200, 50, 90, 950]

salling_products_zip = zip(items, prises)
salling_products_list = list(salling_products_zip)
print(salling_products_list)