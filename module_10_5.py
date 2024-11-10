from threading import Thread
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name,"r", encoding="utf-8") as file:
        while True:
            content = file.readline()
            if not content:
                break
            all_data.append(content)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = datetime.now()
for filename in filenames:
    read_info(filename)
print("Время линейного выполнения:", datetime.now() - start_time)

# Многопроцессный
# if __name__ == '__main__':
#     start_time = datetime.now()
#     with multiprocessing.Pool() as pool:
#         pool.map(read_info, filenames)
#     print("Время многопроцессного выполнения:", datetime.now() - start_time)