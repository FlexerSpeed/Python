from pathlib import Path

file = open('test.txt', 'w')  # Создание файла
file.close()

my_file = Path('test.txt')

if my_file.exists():
    my_file.unlink()  # unlink метод удаления файла
