"""
By defination Polymorphism is chracterstic of an entity to be able to present in more than one form.
Consider Identical TWIN they both look the same but dont behave the same.That exactly Polymorphism works in Programming.
We have a '+' operater which performne addition for 'int' by concate in 'str'.So here you can see that 
this operater looks the same but behave diffrently.
So lets discuss the one property of Polymorphism named as Overriding.Lets discuss the example of inhertance.
We have a person who play basketball and he has a son so his son as inherting the features he also play basketball
but not exactly as his father play.You have your own custom style in which you play basketball.
Now overriding is when a derived class is inherit method from its base class but then it might not be behave in the same
way in your derived class.Your Derived class has the abilty to change the behaviour how this method work by 
redefining inderived class
"""
class Employee:
	def setHour(self):
		self.noofworkinghour = 40
	def displayHour(self):
		print(self.noofworkinghour)

emp = Employee()
emp.setHour()
print("The no of working hour of the emplyee is ")
emp.displayHour()

#lets create a new class which is inherting all the attributes and method from Employee class.

class Trainee(Employee):
	#redefining the method which is availble in base class 
	def setHour(self):
		self.noofworkinghour = 45

tr = Trainee()
tr.setHour()
print("No of working hour of the trainee is ")
tr.displayHour()

#if you want to call the base class method in python you can perform with the help of a super method.
#in our next example you will also learn more about the super method , the use cases as well.
class Trainee1(Employee):
	#redefining the method which is availble in base class 
	def setHour(self):
		self.noofworkinghour = 45

	def resetHour(self):
		super().setHour()

t = Trainee1()
t.setHour()
print("No of working hour of trainee ")
t.displayHour()
print("Let me reset it ")
t.resetHour()
print("Now the working hour will be ")
t.displayHour()