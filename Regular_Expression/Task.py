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
        return (False, "No white spaces!")

    if not re.fullmatch(password_len_pattern, password):
        return (False, "Password must have 8 symbolse")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have lovercase leter")

    if not re.fullmatch(appercase_pattern, password):
        return (False, "Password must have appercase leter")

    if not re.fullmatch(numbers_pattern, password):
        return (False, "Password must have number")

    if not re.fullmatch(symbols_pattern, password):
        return (False, "Password must have symbol")

    return (True, 'Password exepted!')


print(check_passwod_way2('Absbdsdsds12@   '))
