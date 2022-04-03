"""
    https://www.youtube.com/watch?v=7aHjkGFtbnM&list=PLSc7xcwCGNh3Ls-WARhH54WwiqB91Kyak&ab_channel=FranciscoRodrigues
    min 24:14
"""

from unittest import result
import numpy as np 
import math
import unittest

class Probability_B():
    def Num_To_Probability(self, numMath, numEnglish, numMathEnglish, numNone):
        probabilities = []
        if((numMathEnglish > numMath) or (numMathEnglish > numEnglish)):
            return probabilities
        if((numMath < 0) or (numEnglish < 0) or (numMathEnglish < 0) or (numNone < 0)):
            return probabilities
        total = int(numMath) + int(numEnglish) + int(numNone)
        probabilities = [int(numMath) / total, int(numEnglish) / total, int(numMathEnglish) / total, int(numNone) / total]
        return probabilities

class Tests(unittest.TestCase):
    def test_Num_To_Probability_numMathEnglish_bigger(self):
        self.assertEqual(len(Probability_B.Num_To_Probability(Probability_B, 10, 10, 11, 5)),  0, "Should be 0")
    def test_Num_To_Probability_numMath_neg(self):
        self.assertEqual(len(Probability_B.Num_To_Probability(Probability_B, -10, 10, 11, 5)),  0, "Should be 0")
    def test_Num_To_Probability_numEnglish_neg(self):
        self.assertEqual(len(Probability_B.Num_To_Probability(Probability_B, 10, -10, -11, 5)),  0, "Should be 0")
    def test_Num_To_Probability_numMathEnglish_neg(self):
        self.assertEqual(len(Probability_B.Num_To_Probability(Probability_B, 10, 10, -11, 5)),  0, "Should be 0")
    def test_Num_To_Probability_numNone_neg(self):
        self.assertEqual(len(Probability_B.Num_To_Probability(Probability_B, 10, 10, 11, -5)),  0, "Should be 0")
    def test_Num_To_Probability_numAll_neg(self):
        self.assertEqual(len(Probability_B.Num_To_Probability(Probability_B, -10, -10, -11, -5)),  0, "Should be 0")
    def test_Num_To_Probability_normal(self):
        self.assertEqual(Probability_B.Num_To_Probability(Probability_B, 4, 4, 1, 2),  [0.4, 0.4, 0.1, 0.2], "Should be [0.4, 0.4, 0.1, 0.2]")
    def test_Num_To_Probability_broken_num(self):
        self.assertEqual(Probability_B.Num_To_Probability(Probability_B, 4.5, 4.9, 1.1, 2.4),  [0.4, 0.4, 0.1, 0.2], "Should be [0.4, 0.4, 0.1, 0.2]")
    
if __name__ == '__main__':
    unittest.main()