from pathlib import Path


def create_folder(folder_name, folder_way):
    path = Path(folder_way) / folder_name
    if not path.exists():
        path.mkdir()
        print(f'{folder_name} in {folder_way} has created')
    else:
        print(f'{folder_name} in {folder_way} already created')


folder_name = 'Task_folder'
folder_way = './File_Manipulations'
create_folder(folder_name, folder_way)


file_path = './File_Manipulations/Task_folder/'

with open(Path(file_path) / 'file1.txt', 'w') as first_file:
    first_file.write('First string\n')
    first_file.write('Second string\n')
    first_file.write('Third string\n')

with open(Path(file_path) / 'file1.txt') as first_file:
    print(first_file.read())

with open(Path(file_path) / 'file2.txt', 'w') as second_file:
    lines = ['First line', 'Second line', 'Third line']
    for line in lines:
        second_file.write(f'{line}\n')

with open(Path(file_path) / 'file2.txt') as second_file:
    lines = second_file.readlines()
    for line in lines:
        print(line)

# Функция для удаления


def delet_file(file_name, file_way):
    file_path = Path(file_way) / file_name
    if file_path.exists():
        file_path.unlink()
    else:
        print(f'{file_name} in {file_way} isnt exist')


first_file = Path(file_path) / 'file1.txt'
first_file.unlink()
