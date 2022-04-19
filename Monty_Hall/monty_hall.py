from unittest import result
import unittest

import numpy as np
import random

ERROR_TAG = "Error"

def Door_Generator(numberOfDoors):
    if(isinstance(numberOfDoors, int)):
        if(numberOfDoors > 2):
            doors = list(np.zeros((numberOfDoors)).astype(int))
            i = random.randint(0,numberOfDoors)
            doors[i] = 1
            return doors
    return ERROR_TAG




if __name__ == '__main__':
    Door_Generator(5)