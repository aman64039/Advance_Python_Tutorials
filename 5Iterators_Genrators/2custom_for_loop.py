"""
custom for loop
for i in [1,2,3]
for i in "Hello"
so as we got the concept for loop firstly convert iterable into itrator then call next method on it.
so lets have a look how we can make our own custmize for loop.
"""

def my_for(iterable):
	iterator = iter(iterable)
	while True:
		try:
			print(next(iterator))
		except StopIteration:
			#when the elemnts ended in iterator and we call next so it will raise an error 
			#named as StopIteration so we are handling it if we got this error then stop the loop.
			break

my_for("Amanpreet Singh")
my_for([10,20,30,40,50,60,70,80,90,100])



#Another way we can do is
def my_for(iterable):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			#when the elemnts ended in iterator and we call next so it will raise an error 
			#named as StopIteration so we are handling it if we got this error then stop the loop.
			break
		else:
			print(thing)

my_for("Amanpreet Singh")
my_for([10,20,30,40,50,60,70,80,90,100])

#Another Example
def my_for(iterable):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			#when the elemnts ended in iterator and we call next so it will raise an error 
			#named as StopIteration so we are handling it if we got this error then stop the loop.
			break
		else:
			func(thing)

def square(x):
	print(x*x)

my_for([10,20,30,40,50,60,70,80,90,100],square)