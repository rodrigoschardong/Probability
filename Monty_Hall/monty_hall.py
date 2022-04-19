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

def Door_Check(doors, chosenDoor):
    if(chosenDoor < len(doors)):
        return doors[chosenDoor]
    return 0





if __name__ == '__main__':
    numberOfDoors = 5
    doors = Door_Generator(numberOfDoors)
    print(doors)
    index = random.randint(0, numberOfDoors)
    print("Chosen door:", index)
    doorChecked = Door_Check(doors, index)
    print("Door",index,"result",doorChecked)