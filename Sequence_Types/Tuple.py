# Tuple Кортежи

# Кортеж это упорядоченная последрвательность элементов
# Кортеж это неизменяемый тип обьекта (удаление, изменение невозможно)
# Своего рода константа

my_nums = (10, 5, 11, 1)

fruit_1 = 'apple'
fruit_2 = 'banana'
fruit_3 = 'mango'
fruits = (fruit_1, fruit_2, fruit_3)  # составления кортежа из переменных

total = my_nums + fruits  # обьединение кортежей

print(total.count(10))  # метод посдсчета указанного значения
print(total.index(1))  # метод опредедения индекса згачения в кортеже

# cпособ изменения кортежа при его конвертации в лист и обратно в кортеж
list_for_change = list(my_nums)
list_for_change.append(400)
my_nums = tuple(list_for_change)
print(my_nums)
