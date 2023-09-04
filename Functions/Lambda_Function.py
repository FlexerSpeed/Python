# --- Lambda Functions --- ?????????????????

# Синтаксис lambda parameters: expression
# Принимает только одно выражения
# Анинонимны (имя функции отсутсвует)

def mult(a, b):  # Классическая функция
    return a * b


def lambda_mult(a, b): return a * b  # Вариант лямбда функции


print(lambda_mult(5, 2))


def greeting(greet):
    return lambda name: f'{greet}, {name}!'


# Записываем значение для внешней функции в переменную
morning_greet = greeting('Good morning')
print(morning_greet('Michael'))  # Используем внутреннюю лямба функцию


# --- замыкания функций (closure)??????
