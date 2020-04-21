"""
map: a built in function called map which we can use lambdas with and its pretty comman use case for them.
Map is a standard function which accpets at least 2 arguments , a function and an iterable.
Iterable - something that can be iterated over (list , str , dictionary , sets , tuple).
Runs the lambda or any function for each value in the iterable and return a map object which 
can be converted into another data structer.
so lets take an example i have a list which consist of some values and i want to square all the element
for this concept we can use loop and the same task we can implement by the map function as well.
so lets understand the concept
"""
l = [10,20,30,40,50,60,70,80,90,100]

#one way to get the squared list
sl = []
for i in l:
	sl.append(i**2)
print(sl)

#lets have a look on map function without use of lambda 

def square(num):
	return num**2

#as map take 2 arguemnts first one as function and 2nd the itrable object
ml = map(square,l)
#it will return a map object as its mention in the defination which we had mention on the top
#so we have to convert it into a list 
ml = list(ml)
#or we can use it like this
ml = list(map(square,l))
print(ml)

#lets have a look on map function with use of lambda 

ll = list(map(lambda x: x**2 ,l ))
print(ll)

#Another Example
people = ["Aman","Preet","Amrit","Deep"]
up = list(map(lambda a : a.upper(),people))
print(up)

#Another Fine Example
names = [{'first':"Aman","last":"Preet"},
		{"first":"Amrit","last":"Pal"}]
first_name = list(map(lambda x: x['first'],names))
print(first_name)
