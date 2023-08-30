# --- Docstring ---

# Является строкой документации, является первой строкой внутри функции
# Описывает, обьясняет функцию, параметры и т.д
# Является хорошей практикой, т.к делают код более достпным и понятным

def mult_by_factor(value, mult=1):
    """Multiplies number by multiplicator""" # Указыаем описание для функции
    return value * mult

mult_by_factor(5)


def print_number_info (num):
    """
    Prints num information                 

    Args:
        num (int): integer number

    Returns:
        int: Same number
    """ # Так же добавляем описание для аргументов  
    if (num % 2) == 0:
        print('Entered number is even')
    else:
        print('Entered nuber is odd')

    return num


print_number_info(20)