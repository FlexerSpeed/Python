# Чтение файлов


# with open('text.txt') as test_file:
# print(test_file.read())  # read Читает текст файла
# read lines выдает строки в списке. каждая строка является элементом
# print(test_file.readlines())

with open('text.txt', 'w') as new_file:  # Запись в файл. Необходимо указывать второй аргумент W
    # При аргументе W записи всё содержимое перзапишется
    new_file.write('First liine is new\n')
    new_file.write('Second liine is new\n')

with open('text.txt', 'a') as new_file:  # Аргумент a записывает строку последней в текст
    new_file.write('Third line is new\n')  # Сохраняет содержимое

with open('text.txt') as new_file:  # При использовании WITH метод CLOSE вызывается атоматически
    print(new_file.read())

with open('text.txt') as test_file:
    for line in test_file:
        print(line)
