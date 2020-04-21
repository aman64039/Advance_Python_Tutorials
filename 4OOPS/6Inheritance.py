#please find the pdf file in the same directory

#simple inheritance
#base class
class Apple:
	manufacturer = "Apple Inc."
	contactwebsite = "www.apple.com/contact"

	def contactDetails(self):
		print("The contact link is ",self.contactwebsite)

#inheritnig from class Apple
#derived class
class MacBook(Apple):
	def __init__(self):
		self.yearofmanufacture = 2016

	def manufacturerdetails(self):
		print(f"Macbook is manufactured in {self.yearofmanufacture} by {self.manufacturer}")
"""
As we know firstly python check about instance attribute if its found that printed otherwise it will
check to class attributes but if its also not founded then it will check the attributes of base class.
"""
#object of derived class
mac = MacBook()
#method of derived class
mac.manufacturerdetails()
#method of base class
mac.contactwebsite()

#Multiple Inheritance
#Inheriting the properties from 2 classes is known as Multiple Inheritance
class Os:
	multitask = True
	name = "Mac os "

class Apple:
	webiste = "www.apple.com"
	name = "Apple"

class MacBook(Os,Apple):
	def __init__(self):
		if self.multitask:
			print(f"This is multitasking system. Visit {self.webiste} for more details")
			print(self.name)
			#it will print the value of class which is inherited first in our case its Os
			#rest we will discuss in the concept of Polymorphism

#object of derived class which is derived from Os, Apple class
mac = Macbook()


#Multilevel Inheritance
    class Animal:  
        def speak(self):  
            print("Animal Speaking")  
    #The child class Dog inherits the base class Animal  
    class Dog(Animal):  
        def bark(self):  
            print("dog barking")  
    #The child class Dogchild inherits another child class Dog  
    class DogChild(Dog):  
        def eat(self):  
            print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  