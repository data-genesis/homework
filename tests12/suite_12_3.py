import unittest
import tests_12_3

runTest = unittest.TestSuite()

runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runTest.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

testGoRun = unittest.TextTestRunner(verbosity=2)
testGoRun.run(runTest)


