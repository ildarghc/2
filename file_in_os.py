import os
import time

directory = 'C:\\Users\\ildar\\PycharmProjects\\pythonProject1'
for path, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(path, file)
        file_mod_time = time.ctime(os.path.getmtime(file_path))
        file_size = os.path.getsize(file_path)
        file_dir = os.path.basename(os.path.dirname(file_path))
        print(f'Файл {file}:\n- путь: {file_path}\n- время последнего изменения: {file_mod_time}'
              f'\n- размер: {file_size} байт\n- родительская папка: {file_dir}')
