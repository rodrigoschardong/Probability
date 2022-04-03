# A_coin_probability.py

https://www.youtube.com/watch?v=7aHjkGFtbnM&list=PLSc7xcwCGNh3Ls-WARhH54WwiqB91Kyak&index=1&t=452s&ab_channel=FranciscoRodrigues 
## 	There are three functions in Probability_A class

​		**Toss_A_Coin**: Receive the probability to return *true*. It receives the probability param that needs to have a value between 0 and 1 to return *true* or *false* (1 or 0)

​		**Frequency**: It's receive an list of zeros and ones to respond with a probability to find a one in this list. This function returns a float with a value between 0 and 1 

​		**Experiment**: This function is the main experiment from this class. It receives the probability to use the Toss_A_Coin function and the number of chances that the coin will be toss. It return a list of results of zeros and ones.

​		**Frequencies**: It's produces an list of frequencies generated for each number of coins tossed between one and the param maxChanges. These frequencies are based on the probability given by the param probability. This function returns a list that the index is the number of coins tossed for each frequency.

## 	These functions are tested with Test Class. 

​		When this script runs, Test Class runs too. Actually,  this script is to be imported by another script to use the Probability_A_class. So, if you run this script, you will just test it and see if it's ok to use.

# notebook.ipynb

​	Using ipywidgets and matplotlib libraries, you can interact with functions from Classes created.