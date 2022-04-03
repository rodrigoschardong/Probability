"""
    https://www.youtube.com/watch?v=7aHjkGFtbnM&list=PLSc7xcwCGNh3Ls-WARhH54WwiqB91Kyak&ab_channel=FranciscoRodrigues
    min 7:46
"""

from unittest import result
import numpy as np 
import math
import unittest

class Probability_A():
    """
    @brief  It's like toss a coin
    @note   Return true or false
    @params probability: probability to return true
    @retval one or zero (binary)
    """
    def Toss_A_Coin(self, probability):
        if(np.random.uniform() < probability):
            return 1
        else:
            return 0

    def Frequency(self, results):
        trueAnswer = 0
        for i in range(len(results)):
            if(results[i] == 1):
                trueAnswer += 1
        return trueAnswer / len(results)

    def Experiment(self, probability, chances, TEST = 0):
        if(chances != math.trunc(chances)):
            chances = math.trunc(chances)
        results  = []
        for i in range (chances):
            if(TEST == 1):
                results.append(self.Toss_A_Coin(Probability_A, probability))
            else:
                results.append(self.Toss_A_Coin(probability))

        return results

    def Frequencies(self,probability, maxChances, TEST = 0):
        simulations = []
        for c in range (1, int(maxChances) + 1):
            if(TEST == 0):
                simulations.append(self.Frequency(self.Experiment(probability, c)))
            else:
                simulations.append(self.Frequency(Probability_A, self.Experiment(Probability_A, probability, c, 1)))
        return simulations

class Tests(unittest.TestCase):

    def test_Toss_A_Coin_zero_percent(self):
        self.assertEqual(Probability_A.Toss_A_Coin(Probability_A, 0),  0, "Should be 0")       
    def test_Toss_A_Coin_hundred_percent(self):
        self.assertEqual(Probability_A.Toss_A_Coin(Probability_A, 1),  1, "Should be 1")

    def test_Frequency_zero(self):
        self.assertEqual(Probability_A.Frequency(Probability_A, [0,0,0,0,0,0]),  0, "Should be 0")
    def test_Frequency_half(self):
        self.assertEqual(Probability_A.Frequency(Probability_A, [0,1,0,1,0,1]),  0.5, "Should be 0.5")
    def test_Frequency_one(self):
        self.assertEqual(Probability_A.Frequency(Probability_A, [1,1,1,1,1,1]),  1, "Should be 1")

    def test_Experiment_zero(self):
        self.assertEqual(len(Probability_A.Experiment(Probability_A, 0, 0, 1)),  0, "Should be 0")
    def test_Experiment_five(self):
        self.assertEqual(len(Probability_A.Experiment(Probability_A, 0, 5, 1)),  5, "Should be 5")
    def test_Experiment_hundred(self):
        self.assertEqual(len(Probability_A.Experiment(Probability_A, 0, 100, 1)),  100, "Should be 100")
    def test_Experiment_negative(self):
        self.assertEqual(len(Probability_A.Experiment(Probability_A, 0, -1, 1)),  0, "Should be 0")
    def test_Experiment_broken_num(self):
        self.assertEqual(len(Probability_A.Experiment(Probability_A, 0, 2.5, 1)),  2, "Should be 2")
    def test_Experiment_negative_broken_num(self):
        self.assertEqual(len(Probability_A.Experiment(Probability_A, 0, -2.5, 1)),  0, "Should be 0")
    
    def test_Frequencies_zero(self):
        self.assertEqual(len(Probability_A.Frequencies(Probability_A, 0, 0, 1)),  0, "Should be 0")
    def test_Frequencies_negative(self):
        self.assertEqual(len(Probability_A.Frequencies(Probability_A, 0, -1, 1)),  0, "Should be 0")
    def test_Frequencies_five(self):
        self.assertEqual(len(Probability_A.Frequencies(Probability_A, 0, 5, 1)),  5, "Should be 5")
    def test_Frequencies_hundred(self):
        self.assertEqual(len(Probability_A.Frequencies(Probability_A, 0, 100, 1)),  100, "Should be 100")
    def test_Frequencies_broken_num(self):
        self.assertEqual(len(Probability_A.Frequencies(Probability_A, 0, 5.7, 1)),  5, "Should be 5")

if __name__ == '__main__':
    unittest.main()