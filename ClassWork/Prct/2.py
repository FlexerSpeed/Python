# --- Task Two---

def factorial(x):
    if x < 0:
        return '0'
    elif x == 0:
        return '1'
    else:
        result = 1
        factors = []
        for i in range(1, x + 1):
            result *= i
        factors = [char for char in str(result)]
        return ', '.join(factors)


print(factorial(8))
