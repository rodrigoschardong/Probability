from unittest import result
import unittest


class Conditional():
    def Conditional_Formula(self, probAandB, probB):
        if(probB > 0):
            return (probAandB / probB)
        return "Error"

class Tests(unittest.TestCase):
    def test_Conditional_Formula_Error(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 10, 0),  "Error", "Should be Error")
    def test_Conditional_Formula_Zero(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 0, 10),  0, "Should be 0")
    def test_Conditional_Formula_One(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 10, 10),  1, "Should be 1")
    def test_Conditional_Formula_Half(self):
        self.assertEqual(Conditional.Conditional_Formula(Conditional, 0.5, 2),  0.25, "Should be 0.25")

if __name__ == '__main__':
    unittest.main()