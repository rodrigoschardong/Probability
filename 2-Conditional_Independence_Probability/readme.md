# Conditional Probability and Independence

# Conditional.py

https://www.youtube.com/watch?v=HzOCwzzlGiA&list=PLSc7xcwCGNh3Ls-WARhH54WwiqB91Kyak&index=2&ab_channel=FranciscoRodrigues

## 	There are three functions in Conditional class

​		**Conditional_Formula**: Receive the probability of (A intersection B) and probability of B to return the probability conditional (A|B)

​		**Probability**: It's an conjunct and sample universe to returns the probability of this conjunct at the given universe.

​		**Even_And_Odds_Conjunct**: This function receives a simple list of numbers and filters it to return two lists: one with just even numbers and other list with just odds numbers.

​		**Less_Than_Conjunct**: It receives a simple list of values and a threshold value to return in a list just number that are smaller than the threshold.

​		**Greater_Than_Conjunct**: It receives a simple list of values and a threshold value to return in a list just number that are bigger than the threshold.

​		**And_OP_Conjuct**: It receives two conjuncts to find the intersection between them to returns it. These conjuncts can be a simple list or a list of lists. 

​		**Or_OP_Conjuct**: It receives two conjuncts to find the union between them to returns it. These conjuncts can be a simple list or a list of lists.

​		**Not_OP_Conjunct**: This function receives two params as a list each: a conjunct and the universe sample of this conjunct to returns all others elements that aren't in the sample universe. 

​		**Equal_To_Conjunct**: It receives a conjunct as a list and receive a value to be found in this conjunct. This function returns, as a list, all elements on the list that are equal to the value.

## 	These functions are tested with Test Class. 

​		When this script runs, Test Class runs too. Actually,  this script is to be imported by another script to use the Probability_A_class. So, if you run this script, you will just test it and see if it's ok to use.

# notebook.ipynb

​	Using ipywidgets and matplotlib libraries, you can interact with functions from Classes created.

