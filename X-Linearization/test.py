from unittest import result
import unittest
#from Monty_Hall.monty_hall import s
from linearization import Linearization

class Tests(unittest.TestCase):
    def test_init_class(self):
        x = [0,1,2,3,4,5]
        y = [5,4,3,2,1,0]
        lnzt = Linearization(x,y)

        expected = x
        received = lnzt.x
        self.assertEqual(received, expected, "Should be " + str(expected))

        expected = y
        received = lnzt.y
        self.assertEqual(received, expected, "Should be " + str(expected))

    def test_SumOfArray(self):
        x = [0,1,2,3,4,5]
        y = [5,4,3,2,1,0]
        lnzt = Linearization(x,y)

        expected = x[0] + x[1] + x[2] + x[3] + x[4] + x[5]
        received = lnzt._SumOfArray(x)
        self.assertEqual(received, expected, "Should be " + str(expected))

    def test_SumOfProductOfArray(self):
        x = [0,1,2,3,4,5]
        y = [5,4,3,2,1,0]
        lnzt = Linearization(x,y)

        expected = x[0] * y[0] + x[1] * y[1] + x[2] * y[2] + x[3] * y[3] + x[4] * y[4] + x[5] * y[5]
        received = lnzt._SumOfProductOfArray(x, y)
        self.assertEqual(received, expected, "Should be " + str(expected))

    def test_GetAngularCoeficient(self):
        x = [0,1,2,3,4,5]
        y = [0,1,2,3,4,5]
        lnzt = Linearization(x,y)

        lnzt._GetAngularCoeficient(x, y)

        expected = 1
        received = lnzt._A
        self.assertEqual(received, expected, "Should be " + str(expected))

        x = [0,1,2,3,4,5]
        y = [0,2,4,6,8,10]
        lnzt = Linearization(x,y)

        lnzt._GetAngularCoeficient(x, y)

        expected = 2
        received = lnzt._A
        self.assertEqual(received, expected, "Should be " + str(expected))

    def test_GetLinearCoeficient(self):
        x = [0,1,2,3,4,5]
        y = [0,1,2,3,4,5]
        lnzt = Linearization(x,y)

        coeficients = lnzt.Linearization()

        expected = 0
        received = lnzt._B
        self.assertEqual(received, expected, "Should be " + str(expected))

        x = [0,1,2,3,4,5]
        y = [1,2,3,4,5,6]
        lnzt = Linearization(x,y)

        coeficients = lnzt.Linearization()

        expected = 1
        received = lnzt._B
        self.assertEqual(received, expected, "Should be " + str(expected))

if __name__ == '__main__':
    unittest.main()