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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:  # Копия списка для безопасного удаления
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.ycein = Runner("Усейн", speed=10)
        self.andrew = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):  # Исправлено: `cls` вместо `self`
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    def test_ycein_and_nik(self):
        tournament = Tournament(90, self.ycein, self.nik)  # Исправлено: убран `participants=`
        results = tournament.start()
        self.__class__.all_results[1] = results
        self.assertTrue(str(results[max(results)]) == "Ник")  # Исправлено: сравнение через `str`

    def test_andrew_and_nik(self):
        tournament = Tournament(90, self.andrew, self.nik)  # Исправлено: убран `participants=`
        results = tournament.start()
        self.__class__.all_results[2] = results
        self.assertTrue(str(results[max(results)]) == "Ник")  # Исправлено: сравнение через `str`

    def test_all_runners(self):
        tournament = Tournament(90, self.ycein, self.andrew, self.nik)  # Исправлено: правильные имена
        results = tournament.start()
        self.__class__.all_results[3] = results
        self.assertTrue(str(results[max(results)]) == "Ник")  # Исправлено: сравнение через `str`


if __name__ == "__main__":
    unittest.main()
