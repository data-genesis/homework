import unittest
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "True")
    def test_walk(self):
        self.alaska = Runner("alaska")

        for i in range(10):
            self.alaska.walk()
        self.assertEquals(self.alaska.distance, 50)

    @unittest.skipIf(is_frozen, "True")
    def test_run(self):
        self.depech = Runner("depech")
        for i in range(10):
            self.depech.run()
        self.assertEquals(self.depech.distance, 100)

    @unittest.skipIf(is_frozen, "True")
    def test_challenge(self):
        self.blade = Runner("blade")
        self.switch = Runner("switch")
        for i in range(10):
            self.blade.run()
            self.switch.walk()
        self.assertNotEqual(self.blade.distance, self.switch.distance)

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.ycein = Runner("Усейн", speed=10)
        self.andrew = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    @unittest.skipIf(is_frozen, "True")
    def test_ycein_and_nik(self):
        tournament = Tournament(90, self.ycein, self.nik)
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(str(results[max(results)]) == "Ник")

    @unittest.skipIf(is_frozen, "True")
    def test_andrew_and_nik(self):
        tournament = Tournament(90, self.andrew, self.nik)
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(str(results[max(results)]) == "Ник")

    @unittest.skipIf(is_frozen, "True")
    def test_all_runners(self):
        tournament = Tournament(90, self.ycein, self.andrew, self.nik)
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(str(results[max(results)]) == "Ник")


if __name__ == "__main__":
    unittest.main()
