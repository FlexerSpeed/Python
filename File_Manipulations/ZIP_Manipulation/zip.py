# Работа с файлами ZIP
from zipfile import ZipFile
from pathlib import Path

path_to_file = './ZIP_Manipulation/my_files'
zip_path = Path(path_to_file) / 'my-files.zip'

# Создание ZIP файла в директории
# with ZipFile(zip_path, mode='w') as my_zip_file:
#     for file in Path(path_to_file).iterdir():
#         print(file)
#         my_zip_file.write(file)


# РАспаковка архива с помощью Exctractall
with ZipFile(zip_path) as my_zip_file:
    my_zip_file.extractall('./ZIP_Manipulation/my_files-unzipped')
