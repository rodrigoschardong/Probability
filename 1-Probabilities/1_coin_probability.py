"""
    https://www.youtube.com/watch?v=7aHjkGFtbnM&list=PLSc7xcwCGNh3Ls-WARhH54WwiqB91Kyak&ab_channel=FranciscoRodrigues
    min 7:46
"""

from unittest import result
import numpy as np 
import unittest


class Probability():
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
        for i in range(results.shape[0]):
            if(results[i] == 1):
                trueAnswer += 1
        return trueAnswer / results.shape[0]

    def Experiment(self, probability, chances):
        results = np.zeros((chances))
        for i in range (chances):
            results[i] = self.Toss_A_Coin(probability)
        return 
        

class Tests(unittest.TestCase):
    def test_Toss_A_Coin_zero_percent(self):
        self.assertEqual(Probability.Toss_A_Coin(Probability, 0),  0, "Should be 0")
        
    def test_Toss_A_Coin_hundred_percent(self):
        self.assertEqual(Probability.Toss_A_Coin(Probability, 1),  1, "Should be 1")

if __name__ == '__main__':
    unittest.main()