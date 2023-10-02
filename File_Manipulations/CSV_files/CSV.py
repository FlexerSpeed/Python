import csv
from pathlib import Path

path_to_folder = Path('./File_Manipulations/CSV_files')

with open(path_to_folder / 'test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5523, 'Mike', 123])
    writer.writerow([2022, 'Misha', 1233])
    writer.writerow([3521, 'Edward', 1234])
