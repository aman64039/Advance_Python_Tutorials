"""
In this file we are going to discuss brief about the method and self parameters.
So lets discuss an exmple i want to check that the employee has completed his target or not.
For now just understand the logic at the end of the example brief about the self is discussed
"""
class Employee:
	target = 5
	def target_achiver(self,sales):
		if self.target > sales:
			print("Target is not achived ")
		else:
			print("Conrats Your target is achived ")

#creating objects 
emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

#calling method
emp1.target_achiver(3)
emp2.target_achiver(8)
emp3.target_achiver(5)
"""Target is not achived 
Conrats Your target is achived 
Conrats Your target is achived """
#So lets discuss about the self 
"""
As you know the method is nothing just a function inside the class.And you can also absorb the syntax diffrence
between a functiona and method that method consis of one default parameter named as self.
So lets suppose if i am not passing an self in method same as a function
class A:
	def abc():
		print("Hey")
a = A()
a.abc()
So it will return an error which says that 'TypeError: target_achiver() takes 1 positional argument but 2 were given'
that says while definig a method you had passed a parametr but while calling there is nothing as argument of that 
given parameter. This is because if we are calling a method like this 

emp1.targetachiver(5)

that is readed by python interprater convert it in follwing way

Employee.targetachiver(emp1,5)

so here the use of self self is just representing the object.
Instead of self you can use any name but by the convention we have to use self here.
"""
emp1.target_achiver(3)
emp2.target_achiver(8)
emp3.target_achiver(5)
#totally same as 
Employee.targetachiver(emp1,3)
Employee.targetachiver(emp2,8)
Employee.targetachiver(emp3,5)


class Employee:
	def set_name(self,name):
		self.name = name
		#the use if self here is that the attribue to be availbel throughout the lifespam of the object
	def get_name(self):
		print("Name is: ",self.name)
		#here you got the concept with the help of self you can use that attribute in any method 

emp1 = Employee()
emp1.set_name("Aman")
emp1.get_name()


"""
Go to the attached PDF file as well.
Static method and Instance method.
"""
class Student:
	def details(self,name):
		self.name = name
		print("Hey ",self.name)
	@staticmethod
	def message():
		print("Welcome to our School ")

#for the use brief about this static method go to the pdf file attached.