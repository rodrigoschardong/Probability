"""
    https://www.youtube.com/watch?v=7aHjkGFtbnM&list=PLSc7xcwCGNh3Ls-WARhH54WwiqB91Kyak&ab_channel=FranciscoRodrigues
    min 7:46
"""

from unittest import result
import numpy as np 
import math
from scipy.special import factorial
import unittest

#U = 60 num

# 6 num = 5 reais
# 7 num = 35 reais
# 8 num = 140 reais

class Probability_C():
    """
    @brief  It's like toss a coin
    @note   Return true or false
    @params probability: probability to return true
    @retval one or zero (binary)
    """
    def __init__(self, sampleUniverseLen, luckyNumbersLen, errorLog = 1):
        self._sampleUniverseLen = sampleUniverseLen
        self._luckyNumbersLen = luckyNumbersLen
        self._luckNumbers = []

        if(sampleUniverseLen >= luckyNumbersLen):
            for i in range(self._luckyNumbersLen):
                self._luckNumbers.append(self._GenerateLuckyNumbers(self._luckNumbers))
        elif(errorLog):
            print("Invalid parameters: SampleUniverseLen: " + str(sampleUniverseLen) + " < " +str(luckyNumbersLen) + " LuckNumberLen")
        
            
    def _GenerateLuckyNumbers(self, luckNumbers):
        luckNumber = np.random.randint(1, self._sampleUniverseLen + 1)
        f_newNum = 1
        for ln in luckNumbers:
            if(luckNumber == ln):
                f_newNum = 0
                break
        if(f_newNum):
            return luckNumber
        else:
            return self._GenerateLuckyNumbers(luckNumbers)
    
    def _Calculate_ProbabilityToWin(self, purchasedLuckyNumbersLen):
        # Combinações de 6 corretos entre 6 sorteados
        combinations_6_correct_out_of_6_drawn = 1

        # Total de combinações possíveis de sortear 6 entre 60
        total_combinations_6_from_60 = math.comb(self._sampleUniverseLen, self._luckyNumbersLen)

        # Combinações de 1 incorreto entre 54
        combinations_1_incorrect_out_of_54 = math.comb(self._sampleUniverseLen - self._luckyNumbersLen, purchasedLuckyNumbersLen - self._luckyNumbersLen)

        # Total de combinações possíveis de escolher 1 entre 60
        total_combinations_1_from_60 = math.comb(self._sampleUniverseLen, 1)

        # Calculando a probabilidade
        probability_to_win = (combinations_6_correct_out_of_6_drawn / total_combinations_6_from_60) * (combinations_1_incorrect_out_of_54 / total_combinations_1_from_60)
        return probability_to_win

    def Plays(self, purchasedLuckyNumbersLen, numberOfPlays):
        output = []
        probabilityToLose = 1
        for play in range(numberOfPlays):
            probabilityToLose = probabilityToLose * (1 - self._Calculate_ProbabilityToWin(purchasedLuckyNumbersLen))
            output.append(1 - probabilityToLose)
        return output

class Tests(unittest.TestCase):

    def test_default(self):
        result = 1 + 1
        expected = 2
        text = "Should be " + str(expected)
        self.assertEqual(result ,  expected, text)

    def test_GenerateLuckyNumbers_MoreLuckyNumbersThanSampleUniverse(self):
        sampleUniverseLen = 10
        luckyNumbersLen = 11
        lottery = Probability_C(sampleUniverseLen, luckyNumbersLen, 0)

        result = lottery._luckNumbers
        expected = []
        text = "Should be " + str(expected)
        self.assertEqual(result ,  expected, text)

    def test_GenerateLuckyNumbers_Len_Of_LuckyNumbers_1(self):
        sampleUniverseLen = 10
        luckyNumbersLen = 5
        lottery = Probability_C(sampleUniverseLen, luckyNumbersLen)

        result = len(lottery._luckNumbers)
        expected = luckyNumbersLen
        text = "Should be " + str(expected)
        self.assertEqual(result ,  expected, text)

    def test_GenerateLuckyNumbers_Len_Of_LuckyNumbers_2(self):
        sampleUniverseLen = 10
        luckyNumbersLen = 10
        lottery = Probability_C(sampleUniverseLen, luckyNumbersLen, 0)

        result = len(lottery._luckNumbers)
        expected = luckyNumbersLen
        text = "Should be " + str(expected)
        self.assertEqual(result ,  expected, text)

    def test_GenerateLuckyNumbers_InSampleUniverse(self):
        sampleUniverseLen = 80
        luckyNumbersLen = 50
        lottery = Probability_C(sampleUniverseLen, luckyNumbersLen)

        results = lottery._luckNumbers
        expectedGreater = 1
        textGreater = "Should be " + str(expectedGreater)

        expectedLesser = sampleUniverseLen + 1
        textLesser = "Should be " + str(expectedLesser)
        for result in results:
            self.assertGreaterEqual(result, expectedGreater, textGreater)
            self.assertLessEqual(result, expectedLesser, textLesser)


if __name__ == '__main__':
    unittest.main()