#one type of higher order function that accepts a function as an argument one or more function.

def sum(n,func):
	total = 0
	for i in range(n):
		total+=func(i)
	return total

def square(x):
	return x*x

print(sum(3,square))


#Another type of higher order functions that is return another function
from random import choice
def greet(name):
	def get_mood():
		msg = choice(("Hello","Hy","Bbye"))
		return msg
	result = get_mood() + ' '+name
	return result

print(greet("Amanpreet"))

#Another Example
def make_laugh():
	def get_laugh():
		l = choice(("hahahahah","heheheheh","lol"))
		return l
	return get_laugh

laugh = make_laugh()
print(laugh())

#Another Example
def make_laugh_at_func(name):
	def get_laugh():
		l = choice(("hahahahah","heheheheh","lol"))
		return f"{l} {name}"
	return get_laugh

laugh_at = make_laugh_at_func("Aman")
print(laugh_at())
