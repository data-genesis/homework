import time
from threading import Thread
from datetime import datetime
from time import sleep


def write_words(word_count, file_name):
    time_start = datetime.now()
    with open(file_name, "a", encoding="utf-8") as file:
        for num in range(1, word_count + 1):
            file.write(f"Какое-то слово № {num}\n")
            sleep(0.1)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(f"Завершилась запись в файл {file_name}")

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_start2 = datetime.now()
first = Thread(target=write_words, args=(10, "example5.txt"))
second = Thread(target=write_words, args=(30, "example6.txt"))
third = Thread(target=write_words, args=(200, "example7.txt"))
fourth = Thread(target=write_words, args=(100, "example8.txt"))

first.start()
second.start()
third.start()
fourth.start()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2

print(f"Потоки закончили работу за {time_res2} секунд.")


