# --- Циклы ---

# Циклы позволяют выполнять один и тот же блок кода несколько раз в зависимости от условий
# Циклы = важная часть програмирования исп. для автомотизации процессов, требующих повторения
# Циклы используются для перебора последовательностей (dict, set, list, tuple, sting)


# Цикл FOR ... IN
# for Элемент in Последовательность:
#    Действие с каждым элементом

# Для списка
my_list = [True, 10, 'abc', {}]  #
for elem in my_list:
    print(elem)

my_object = {  # Для словаря
    'x': 10,
    'a': 20,
    'y': True,
    'z': 'abc'
}

# Вариант 1
for item in my_object.items():  # Метод items специально для словарей, ключ: значение в кортеж
    key, value = item  # Производим распаковку кортежа в переменные
    print(key, ':', value)

# Вариант 2  ИСПОЛЬЗУЕТСЯ ОЧЕНЬ ЧАСТО
for key, value in my_object.items():
    print(key, value)

# FOR ... IN для строк
my_name = 'Michael'  # Разбивает строку на буквы
for char in my_name:
    print(char, end=' ')


# FOR ... IN для наборов
video_ids = {1432, 4590, 3434, 1478}
for id in video_ids:
    print(id, end=' ')


# --- Practical Task ---
def dic_to_list(dic):
    result_list = []
    for k, v in dic.items():
        # if isinstance(v, int):  # isinstance метод проверяющий на пренадлежность к типу данных но он определяет bool как 0 или 1
        if type(v) == int:
            v *= 2
        result_list.append((k, v))
    print(result_list)


dic_to_list(my_object)

test_list = [1, 'kmn', True, 3]


def filter_list(input_list, type_of_value):
    new_list = []
    for i in input_list:
        if type(i) == type_of_value:  # Используем метод type определяющий тип значения
            new_list.append(i)
    return new_list


print(filter_list([1, 'kmn', True, 3], bool))

# Решение через Filter
# Метод Filter используется для фильтрации последовательностей
# В методе нужно указывать функцию, которая будет проводить фильтрация последовательности
# filter(функция, последовательность)


def filter_list_with_filter(input_list, type_of_value):
    '''
    Эта функция использует встроенную функцию filter() для фильтрации элементов
    списка input_list по типу type_of_value.

    Параметры:
    - input_list: Список, который нужно отфильтровать.
    - type_of_value: Тип данных, по которому будет производиться фильтрация.

    Функция создает итератор, который включает только элементы из input_list, которые
    имеют тип, совпадающий с type_of_value. Для сравнения типов используется лямбда-
    функция, которая принимает элемент e из input_list и проверяет его тип с помощью
    функции type().

    После выполнения фильтрации, функция конвертирует результат в список с помощью
    list() и возвращает его.

    '''
    return list(filter(lambda e: type(e) is type_of_value, input_list))


res = filter_list_with_filter([1, 'kmn', True, 3], bool)
print(res, 'Result using "Filter"')
