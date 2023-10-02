# CSV (Comma-Separated Values) - это формат для хранения и передачи табличных данных,
# где значения разделяются запятыми (или другим разделителем) и строки разделяются новыми строками.

import csv
from pathlib import Path

path_to_folder = Path('./File_Manipulations/CSV_files')

# Запсь данных в CSV файл:
# with open(path_to_folder / 'test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5523, 'Mike', 123])
#     writer.writerow([2022, 'Misha', 1233])
#     writer.writerow([3521, 'Edward', 1234])


# Чтение файлов CSV:
with open(path_to_folder / 'test.csv') as csv_file:
    # Создаем ридер. Delimeter это разделитель для данных
    reader = csv.reader(csv_file)
    for line in reader:
        if len(line) == 0:  # Отсеиваем пустые списки
            continue
        else:
            print(line)
