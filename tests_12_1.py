import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.alaska = Runner("alaska")
        for i in range(10):
            self.alaska.walk()
        self.assertEquals(self.alaska.distance, 50)

    def test_run(self):
        self.depech = Runner("depech")
        for i in range(10):
            self.depech.run()
        self.assertEquals(self.depech.distance, 100)

    def test_challenge(self):
        self.blade = Runner("blade")
        self.switch = Runner("switch")
        for i in range(10):
            self.blade.run()
            self.switch.walk()
        self.assertNotEqual(self.blade.distance, self.switch.distance)

if __name__ == '__main__':
    unittest.main()