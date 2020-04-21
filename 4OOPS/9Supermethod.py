"""
In Python, super() has two major use cases:

Allows us to avoid using the base class name explicitly
Working with Multiple Inheritance
"""
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age 
	def display(self):
		print("Name: ",self.name)
		print("Age: ",self.age)


class Student(Person):
	def __init__(self,name,age,roll,marks):
		self.name = name
		self.age = age 
		self.roll = roll
		self.marks = marks 
	def display(self):
		print("Name: ",self.name)
		print("Age: ",self.age)
		print("Roll: ",self.roll)
		print("Marks: ",self.marks)

class Teacher(Person):
	def __init__(self,name,age,salary,subject):
		self.name = name
		self.age = age 
		self.salary = salary
		self.subject = subject 
	def display(self):
		print("Name: ",self.name)
		print("Age: ",self.age)
		print("Salary: ",self.salary)
		print("Subject: ",self.subject)


std = Student('aman',29,102,95)
tec = Student('Aman',39,500000,'Python')

"""
Here you can see this we are initlizing the 2 attributes name and age again and again which we can
also pick out from our base class.So this define the use of super method.
That from base class we want to pick some of the attributes to our derived class while initlizing.
In the follwing Example you will proper got the idea of super().
"""

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age 
	def display(self):
		print("Name: ",self.name)
		print("Age: ",self.age)


class Student(Person):
	def __init__(self,name,age,roll,marks):
		#calling a supper method which says to use init method from base class
		super().__init__(name,age)
		self.roll = roll
		self.marks = marks 

	def display(self):
		super().display()
		print("Roll: ",self.roll)
		print("Marks: ",self.marks)


class Teacher(Person):
	def __init__(self,name,age,salary,subject):
		super().__init__(name,age)
		self.salary = salary
		self.subject = subject 
	def display(self):
		super().display()
		print("Salary: ",self.salary)
		print("Subject: ",self.subject)


std = Student('aman',29,102,95)
tec = Student('Aman',39,500000,'Python')


std.display()
tec.display()
