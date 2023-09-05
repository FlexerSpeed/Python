# ГЕНЕРАЦИЯ ОШИБОК (это создание ошибки для своих условий кода при помощи RISE)
'''
def divide_nums(a, b):
    if b == 0:  # сохдание условия для ошибки
        raise TypeError('Second argument cant be 0')  # Создание ошибки
    return a / b
'''

# ОБРАБОТКА ОШИБОК (позволяет корректно реагировать на аварийные ситуации и избежать аварийного завершения кода)
# Это важная часть написания кода
try:
    # Выполнение блока кода
    print(10 / 0)
except ZeroDivisionError as e:
    # Этот блок выполняется в случае возникновения ошибок в блоке try
    print(e)
except TypeError as e:  # Запрос на указание типа ошибки
    print(e)
# Exeption это общий класс для всех ошибок(универсальный)
except Exception as e:
    print(e)
else:  # Так же можно добавлять блок else (ксли ошибок нет)
    print('No errors')
finally:  # Выполняется всегда!!!
    print('Continue...')
# Выполнение кода продолжается далее в отличии от варианта без оброботки ошибки


# ---Practical Task---

def image_info(dict):
    dict
    if dict[key] == None:
        raise TypeError(
            f'Image {dict["image_title"]} has id {dict["image_id"]}')
    return dict


dictinon = {'image_id': None, 'image_title': None}

image_info(dictinon)
