"""
Decoraters are the functions.
Decoraters wrap the other function and enhance their behaviour.
Decoraters are the example of higher order function.
Decoraters having their own syntax '@'

Lets have a use case
"""

def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you")
		fn()
		print("Have a great day")
	return wrapper

def greet():
	print("My name is Aman")

#creating an object of be polite function with the same name of another function
greet = be_polite(greet)
greet()
#Here you can see that the functionallity is totally changed.
#so lets have a another example with the decorater syntax

def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you")
		fn()
		print("Have a great day")
	return wrapper

@be_polite
def greet():
	print("My name is Aman")

greet()
#here @be_polite is acting as a decorater which make sense when teh greet function is going to be called
#or invoked firstly it has to  passed as an argument of be_polite function


#Python Decorater with Arguments.
def shout(fn):
	def wrapper(name):
		return fn(name).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi i am {name}"

print(greet("Aman"))

#Lets have a another example
# def shout(fn):
# 	def wrapper(name):
# 		return fn(name).upper()
# 	return wrapper

# @shout
# def order(main,side):
# 	return f"Hi i like the {main}, with a side of {side}"

# print(order("Burger","Fries"))
#will through an error that wrapper take one positional argument but 2 were given
#so lets have a standar decorater pattren
print("\n")
def shout(fn):
	def wrapper(*args,**kwargs):
		return fn(*args,**kwargs).upper()
	return wrapper

@shout
def order(main,side):
	return f"Hi i like the {main}, with a side of {side}"

print(order("Burger","Fries"))