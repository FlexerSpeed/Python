# Модуль re представляет собой метод для работы с регулярными выражениями
# Регулярные выражения - мощный инструмент для работы с текстовой ифнормацией, основанный на шаблонах
import re

my_string = "my name is Michael"
text_for_analys = "Nginx server is a high-performance web. Server and proxy server widely used for serving websites and web applications."

# Search предназначен для поиска совпадений в тексте по заданным параметрам
res = re.search('M....e', my_string)
# Метод для поиска в строке в котором задана начальная и конечная точки поиска
analys = re.search('^N.*high', text_for_analys)
# ^ - Указывает начало, .* - указывает на любое кол. символов между началом и концом

# В регулярных выражениях использую r-строки (все символы переводятся в строку)

# --------------
# Создание патерна при помощи метода COMPILE
# Патерн включает \. - означает поиск до знака точки. $ - означнает конец строки
my_pattern = re.compile(r'^N.*\.$')
my_pattern2 = re.compile(r's....r')

print(my_pattern.search(text_for_analys))
# Метод для поиска всех слов с указанным условием
print(my_pattern2.findall(text_for_analys))


# Способ поиска любого Е-адреса в строке
email_string = "Please send your inquiry to support@example.com."  # Сктрока

# Создание регулярного выражения
mail_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
email_check_pattern = re.compile(
    mail_regexp)                 # Создание паттерна

print(email_check_pattern.search(email_string))


# Функция проверки валидности Е-мейла
def check_email(email):
    mail_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(mail_regexp)
    valid_result = 'valid' if email_check_pattern.fullmatch(
        email) else 'no valid'
    return (email, valid_result)
