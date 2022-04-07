from unittest import result
import unittest


class Conditional():
    def Conditional_Formula(self, probAandB, probB):
        if(probB > 0):
            return (probAandB / probB)
        return "Error"

    def Probability(self, conjunct, sampleUniverse):
        if(len(sampleUniverse) == 0):
            return "Error"
        probability = len(conjunct) / len(sampleUniverse)
        if(probability > 1):
            return "Error"
        return probability

    def Even_And_Odds_Conjunct(self, conjunct):
        even = []
        odd = []
        for i in range(len(conjunct)):
            if((conjunct[i] / 2) == int(conjunct[i] / 2)):
                even.append(conjunct[i])
            else:
                odd.append(conjunct[i])
        return even, odd

    def Less_Than_Conjunct(self, conjunct, value):
        out = []
        for i in range(len(conjunct)):
            if(conjunct[i] < value):
                out.append(conjunct[i])
        return out
        

class Tests(unittest.TestCase):
    def test_Conditional_Formula_Error(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 10, 0),  "Error", "Should be Error")
    def test_Conditional_Formula_Zero(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 0, 10),  0, "Should be 0")
    def test_Conditional_Formula_One(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 10, 10),  1, "Should be 1")
    def test_Conditional_Formula_Half(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 0.5, 2),  0.25, "Should be 0.25")

    def test_Probability_Half(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], [0,1,2,3]),  0.5, "Should be 0.5")
    def test_Probability_One(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], [0,1]),  1, "Should be 1")
    def test_Probability_Zero(self):
        self.assertEqual(Conditional.Probability(Conditional, [], [0,1,2,3]),  0, "Should be 0")
    def test_Probability_Divided_By_Zero(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], []),  "Error", "Should be Error")
    def test_Probability_Conjunct_Bigger_Than_Universe(self):
        self.assertEqual(Conditional.Probability(Conditional, [0,1], [0]),  "Error", "Should be Error")

    def test_Probability_Even(self):
        even, odd = Conditional.Even_And_Odds_Conjunct(Conditional, [1,2,3,4,5])
        self.assertEqual(even,  [2,4], "Should be [2,4]")
    def test_Probability_Odd(self):
        even, odd = Conditional.Even_And_Odds_Conjunct(Conditional, [1,2,3,4,5])
        self.assertEqual(odd,  [1,3,5], "Should be [1,3,5]")

    def test_Less_Than_Conjunct(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [0,1], 1),  [0], "Should be [0]")
    def test_Less_Than_Conjunct_Return_All(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [0,1], 10),  [0,1], "Should be [0,1]")
    def test_Less_Than_Conjunct_Return_Nothing(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [0,1], 0),  [], "Should be []")
    def test_Less_Than_Conjunct_Enter_Emply(self):
        self.assertEqual(Conditional.Less_Than_Conjunct(Conditional, [], 1),  [], "Should be []")

if __name__ == '__main__':
    unittest.main()