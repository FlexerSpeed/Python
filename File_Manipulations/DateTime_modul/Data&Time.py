from datetime import date, time, datetime, timedelta


# Дата
my_date = date(2100, 4, 15)

print(my_date.day)
print(my_date.month)
print(my_date.year)
print(my_date.isocalendar())  # Передаёт дату в кортеже

# Время
my_time = time(18, 10, 45)

print(my_time.hour)
print(my_time.minute)
print(my_time.second)

# Дата + Время
my_data_time = datetime(2100, 4, 15, 18, 10, 45)

print(my_data_time.now())

# Способ форматирования даты/времени
print(my_data_time.strftime('%d-%m-%Y %H-%M-%S'))

# Конвертация строки в дату/время
date_str = '10/12/2222'
converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)

# timedelta позволяет вам выполнять арифметические операции с датами и временем,
# такие как добавление или вычитание интервалов времени.
print(my_data_time + timedelta(days=100, minutes=135))
