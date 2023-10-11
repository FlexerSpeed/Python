# Task
import re

# FIRST WAY
# user_password = input('Please enter Your passwod(must include a-z, A-Z, 0-9, _\nend have a len atlest 8):')


def check_password(password):
    mail_regexp = r"[a-zA-Z0-9_]+$"
    if re.match(mail_regexp, password) and len(password) >= 8:
        return print(password, 'password valid')
    else:
        return print(password, 'password is\'t valid. Must be a-z, A-Z, 0-9, _')

# check_password(user_password)


# SECOND WAY
errors_list = ["Password must have 8 symbolse", "Password must have lovercase leter", "Password must have appercase leter",
               "Password must have number", "Password must have symbol", "No white spaces!"]


def check_passwod_way2(password):
    # Проверка длинны выполняется таким путем
    password_len_pattern = re.compile(r"\S{8,}")
    # + значит что значение должно встречаться хотябы раз в строке
    # Набор символов ^.*abc.*$ означает что от начала до конца строки могут быть любые значения
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")
    appercase_pattern = re.compile(r"^.*[A-Z]+.*$")
    numbers_pattern = re.compile(r"^.*[0-9]+.*$")
    symbols_pattern = re.compile(r"^.*[!@#$%-_]+.*$")
    no_whitespace_pattern = re.compile(r"^\S*$")
    # /$ специальный знак соответсвующий любому непробельному символу (то есть этот патерн исключает проблелы)
    # * обозначает что /$ может повторяться бесеонечное кол-во раз до окончания строки

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, print(errors_list[0]))

    if not re.fullmatch(password_len_pattern, password):
        return (False, print(errors_list[1]))

    if not re.fullmatch(lowercase_pattern, password):
        return (False, print(errors_list[2]))

    if not re.fullmatch(appercase_pattern, password):
        return (False, print(errors_list[3]))

    if not re.fullmatch(numbers_pattern, password):
        return (False, print(errors_list[4]))

    if not re.fullmatch(symbols_pattern, password):
        return (False, print(errors_list[5]))

    return (True, 'Password exepted!')


# THIRD WAY

# Создаём лист кортежей с паттернами и ошибками для них
def check_passwod_way2(password):
    patterns = [(r"\S{8,}", errors_list[0]),
                (r"^.*[a-z]+.*$", errors_list[1]),
                (r"^.*[A-Z]+.*$", errors_list[2]),
                (r"^.*[0-9]+.*$", errors_list[3]),
                (r"^.*[!@#$%]+.*", errors_list[4]),
                (r"^\S*$", errors_list[5])]

# Прогоняем пароль через проверки при помощи цикла
    for pattern, error in patterns:
        if not re.search(pattern, password):
            return False, error
    return True, 'Password exepted!'
# На выходе функция возвращает два значения


# Присваимаем двум переменным два значения которые возвращает фонкция
result, message = check_passwod_way2("Sdsadasdasdasdas9!")
if result:
    print(message)
else:
    print("Password not excepted:", message)
