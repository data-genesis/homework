from threading import Thread

import requests

class Getter(Thread):
    res = []
    THE_URL = "https://binaryjazz.us/wp-json/generator/v1/genre/"
    def run(self):
        response = requests.get(self.THE_URL)
        Getter.res.append(response.json())


threads = []

for i in range(10):
    thread
g = Getter()

g.start()