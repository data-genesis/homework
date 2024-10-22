from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.enemy = 100
        self.name = name
        self.power = power
        self.fighting_days = 0


    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemy > 0:
            time.sleep(1)
            self.fighting_days += 1
            self.enemy -= self.power
            if self.enemy < 0:
                self.enemy = 0

            print(f"{self.name} сражается {self.fighting_days} день(дней)... осталось {self.enemy} воинов.")

        print(f"{self.name} одержал победу спустя {self.fighting_days} день(дней)!")
        print("Все битвы закончились!")





first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
