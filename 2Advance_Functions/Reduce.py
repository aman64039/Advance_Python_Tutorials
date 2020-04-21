"""
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of
 the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.
"""

#one way
from functools import reduce
lis = [10,20,30,40,50]
print(reduce(lambda x,y: x+y,lis))

#second way using operater functions
import operator
print(reduce(operator.add,lis))

#using reduce to compute maximum element from list
print (reduce(lambda a,b : a if a > b else b,lis))  