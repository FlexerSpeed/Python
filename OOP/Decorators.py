# Функция декоратор это функция, которая принимает другую функцию в качестве аргумента и возвращают новуб функцию
# -с изминением или расширением  функционала
# Вызов перед обьявлением @ и названия функции декоратора
# Декораторы универсальны и могут применяться для разных функций

def decorator_function(original_fn):
    # Обычно декоратор делают универсальным, добавляя универсальные параметры
    def wrapper_function(*args, **kwargs):
        # Действие перед выполнения оригинальной функции
        print('Executed before function')

        # Выполнение оригинальной функции
        # Передаем универсальные документы так же и в функцию
        result = original_fn(*args, **kwargs)
        # result этоо результат выполнения основной функции с которым мы можем выполнять любые действия

        # Действие после выполнения оригинальной функции и использования ее результата
        print('Function result:', result)

        return result
    return wrapper_function


@decorator_function
def my_function(a, b):
    print('This is my function!')
    return (a, b)


# Аргументы автоматически передаются в "wrapper_function"
result = my_function(100, 50)
print(result)

# ------------------------------------------------------
# Логирование декораторов: Позволяет записывать информацию оо вызове функции и аспектах её выполнения


def log_function_call(fn):
    def wrapper(*args, **kwargs):
        print(f'Function name: {fn.__name__}')
        print(f'Function arguments are: a = {args}, b = {kwargs}')
        result = fn(*args, **kwargs)
        return result
    return wrapper


@log_function_call
def mult(a, b):
    return a * b


@log_function_call
def sum1(a, b):
    return a + b


print(mult(23, b=45))
print(sum1(2.54, 60))

# --------------------------------------------------------------
# Проверка типов аргументов функции декоратора


def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f'Type of {arg} is {type(arg)}')
        result = fn(*args, **kwargs)
        return result
    return wrapper


@validate_args
def sum_num(a, b):
    return a + b


print(sum_num(54, b='2.0'))
