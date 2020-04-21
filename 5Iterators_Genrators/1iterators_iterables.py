"""
Iterators: An object that can be iterated upon. An object which retruns data, one element at a 
time when next() is called on it.
#Iterated upon : you could think on which we can implement for loop like string , list , tuples.
But Behind the sence there is a method named as next() which is used.When you called a method 
or either for loop called on iterator it return the next item at a time you call.
#But an iterator is the actual object that is being iterarted over using the next function.



Iterable: An object which will return an iterator when iter() is called on it.


"Hello" is an iterable but it is not an iterator.

iter("Hello") retrun a iterator.
Basic idea of for loop is firstly it will call iter() on an iterable object the next()
method is going to be called to get the next items.

Lets have an example
"""
name = "Amanpreet"
#its not an itertor we can check it by calling a next method on it.
next(name) #through an error that its not an iterator

it = iter(name) #return a string iterator object
#on this iterator object we can call next method 
next(it)
#when next() is called on an itrarot the iterator return the next item.
#it keeps doing so until it raise a stopIteration error.

#another case
l = [1,2,3,6]
next(l) #will not work
il = iter(l) #return list iterator
nex(il) #will work