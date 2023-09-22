# JSON - JavaScript Object Notation
import json

# Строка JSON (передаёт обьект)
json_str = '{"id":235, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'

# Строка JSON (передаёт массив)
json_array = '[1, 2, 3]'

# Строка JSON (список словарей)
json_dict_in_list = '[{"a": 1}, {"b": 2}, {"c": 3}]'

# Десериализация(декодирование из JSON)
sneakers = json.loads(json_str)  # Метод конверттрующий строку JSON в словарь
numbers = json.loads(json_array)  # В этот раз конверттрует в лист

print(type(sneakers))
print(sneakers)

print(type(numbers))
print(numbers)

# Сериализация(кодирование в JSON)
# Метод когвертирующий обьект в JSON строку
json_from_dict = json.dumps(sneakers)
print(json_from_dict)
