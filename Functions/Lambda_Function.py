# --- Lambda Functions --- ?????????????????

# Синтаксис lambda parameters: expression
# Принимает только одно выражения
# Анинонимны (имя функции отсутсвует)

def mult(a, b):  # Классическая функция
    return a * b

lambda_mult = lambda a, b: a * b # Вариант лямбда функции

print(lambda_mult(5, 2))

# --- замыкания функций (closure)??????

