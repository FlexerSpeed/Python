from os import path  # Функицональй подход
from pathlib import Path  # ООП подход (более желательный)

print(path.abspath('.'))

way_to_directory = Path('.').absolute()  # '.' относительный путь к файлу
print(way_to_directory)

file_path = Path('text.txt')
print([m for m in dir(file_path) if not m.startswith('_')])

# Формирование путей на Windows:
print(Path('C:/').joinpath('Python311').joinpath('Lib'))

# Проверка присутствия директории или файла
print(Path('text.txt').exists())  # Проверка в директории
print(Path('C:\Python311').exists())  # Проверка по пути к файлу

# Проверка файл или директория
print(Path('text.txt').is_file())  # Проверка файл в директории
# Проверка директории (../ Выход из текщей директории)
print(Path('../Python').is_dir())

# Список файлов и папок
for f in Path('.').iterdir():  # Показывает все файлы в директории
    print(f)

# Создание папки в директории
cwd = Path('/Software_Development') / 'Python' / \
    'django'  # Путь с указанием названия папки
# print(cwd.mkdir())  # Метод для создания папки

# print(cwd.rmdir())  # Метод для удаления папки
