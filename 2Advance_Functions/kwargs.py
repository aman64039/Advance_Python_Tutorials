"""
**kwargs:- Its stands for Kwyword args.Most Popular pronounce it as "QWARGS".And the idea is that its
another special operater we can have as a parameter to a fucntion but rather than just collecting any additional
arguments.
This will do is geather remaining keyword arguments as a dict.Same as args kwargs is just a standard name
you can use any name you want.
"""
def details(**kwargs):
	print(kwargs)

details(name="Amanpreet",Profession="Python Developer")

#another example
def fav_colour(**kwargs):
	for person , color in kwargs.items():
		print(f"{person}'s fav colour is {color}")

fav_colour(aman="red",preet="Black",Singh="White")


#unpacking Dictionary
def display_names(first,second):
	print(f"{first} says hello to {second}")

#display_names("Aman","Preet")
#what if i am passing dict here 
name = {"first":"Aman","second":"Preet"}
# display_names(name)
#through an error TypeError: display_names() missing 1 required positional argument: 'second'

#so here we have to unpack the dictionary here as we had unpack the args but in the case of dict we have to use **
display_names(**name)
#this totaly seems like 
display_names("Aman","Preet")