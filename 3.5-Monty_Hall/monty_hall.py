from unittest import result
import unittest

import numpy as np
import random

ERROR_TAG = "Error"

def Door_Generator(numberOfDoors):
    if(isinstance(numberOfDoors, int)):
        if(numberOfDoors > 2):
            doors = list(np.zeros((numberOfDoors)).astype(int))
            i = random.randint(0,numberOfDoors - 1)
            doors[i] = 1
            return doors
    return ERROR_TAG

def Door_Check(doors, chosenDoor):
    if((0 <= chosenDoor < len(doors))):
        return doors[chosenDoor]
    return 0

def Door_Show_Create(numberOfDoors):
    doorShow = []
    for i in range(numberOfDoors):
        doorShow.append("?")
    return doorShow

def Find_Reward(doors):
    for i in range(len(doors)):
        if(doors[i]):
            return i
    return ERROR_TAG

def Open_Doors(doors, chosenDoor):
    doorShow = list(np.zeros((len(doors))))
    rewardDoor = Find_Reward(doors)
    if(0 <= rewardDoor <= len(doors)):
        doorShow[rewardDoor] = "?"
    if(0 <= chosenDoor <= len(doors) - 1):
        if(chosenDoor != rewardDoor):
            doorShow[chosenDoor] = "?"
        else:
            randomDoor = random.randint(0, len(doors) - 1)
            while(randomDoor == rewardDoor):
                randomDoor = random.randint(0, len(doors) - 1)
            doorShow[randomDoor] = "?"
    return doorShow




if __name__ == '__main__':
    numberOfDoors = 5
    doors = Door_Generator(numberOfDoors)
    print(doors)
    index = random.randint(0, numberOfDoors)
    print("Chosen door:", index)
    doorChecked = Door_Check(doors, index)
    print("Door",index,"result",doorChecked)