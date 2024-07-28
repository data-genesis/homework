import os
import time

directory = r"C:\Users\oracle\Documents\P3913\FormatString\module7"
print("Теущая директория: ", os.getcwd())
# if os.path.exists('.venv/second'):
#     os.chdir('.venv/second')
# else:
#     os.mkdir('.venv/second')
#     os.chdir('.venv/second')
# print('Текущая директория:', os.getcwd())

# print(os.listdir())
# for i in os.walk(".venv"):
#     print(i)

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

