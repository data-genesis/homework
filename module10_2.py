from threading import Thread

import requests


class Getter(Thread):
    res = []
    def __init__(self, url):
        self.THE_URL = url
        super().__init__()
    def ques(self):
        return Getter.res
    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())

threads = []
num_of_genres = 10
for i in range(num_of_genres):
    thread = Getter("https://binaryjazz.us/wp-json/generator/vl/genr")
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(Getter.ques())