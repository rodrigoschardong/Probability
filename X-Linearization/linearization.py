from unittest import result
import unittest

import numpy as np
import random

TAG = "Linearization: "

class Linearization():
    def __init__(self, x, y):
        if(len(x) == len(y)):
            self.x = x
            self.y = y
        else:
            print(TAG + "x and y don't have the same lengh")

    def _SumOfArray(self, array):
        sum = 0
        for val in array:
            sum += val
        return sum
    
    def _SumOfProductOfArray(self, array1, array2):
        sum = 0
        if(array1 >= array2):
            lengh = len(array2)
        else:
            lengh = len(array1)
        for i in range(lengh):
            sum += array1[i] * array2[i]
        return sum
    
    def _GetAngularCoeficient(self):
        lengh = len(self.x)
        dominator = lengh * self._SumOfProductOfArray(self.x, self.y)
        dominator -= (self._SumOfArray(self.x) * self._SumOfArray(self.y))

        denominator = lengh * self._SumOfProductOfArray(self.x, self.x)
        denominator -= (self._SumOfArray(self.x) * self._SumOfArray(self.x))

        self._A = dominator / denominator

    def _GetLinearCoeficient(self):
        lengh = len(self.y)
        y = self._SumOfArray(self.y) / lengh
        x = self._SumOfArray(self.x) / lengh

        self._B =  y - (self._A * x)

    def Linearization(self):
        self._GetAngularCoeficient()
        self._GetLinearCoeficient()

        return {'angular': self._A, 'linear': self._B}


if __name__ == '__main__':
    x = [0,1,2,3,4,5]
    y = [5,4,3,2,1,0]
    Linearization(x, y)