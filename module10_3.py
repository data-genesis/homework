import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            value = randint(50, 501)
            with self.lock:
                self.balance += value
                print(f"Пополнение: {value}. Баланс: {self.balance}")
                if self.balance >= 500:
                    continue
            sleep(0.001)

    def take(self):
        for _ in range(100):
            value = randint(50, 501)
            with self.lock:
                print(f"Запрос на {value}")
                if self.balance >= value:
                    self.balance -= value
                    print(f"Снятие: {value}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')
