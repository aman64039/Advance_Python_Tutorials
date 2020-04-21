# class Employee:
# 	def set_name(self):
# 		self.name = "Aman"
# 	def get_name(self):
# 		print(self.name)


# emp1 = Employee()
# emp1.get_name()
"""
Here you will get an error because when we invoke the method name as set_name which print the self.name
the object was unable to find the instace attribute self.name thats because we called a second method 
before called a first method, the initlization is going to happen in first method which we never called
so we need a mechanism which initlize the attribute before they used and Python perform this task by 
a special method name as init method or initlize method or if you have knowledge of some of the other 
programing languages its totally same as a constructer.This method is first method of the class and be 
invoked by the creation of the object.
"""
#one way
class Employee:
	def __init__(self):
		self.name = "Aman"
	def get_name(self):
		print(self.name)

emp = Employee()
emp.get_name()



#second way
class Student:
	#special method in python always start and end with __ (2 underscore)
	def __init__(self,fname,lname):
		self.name = fname+lname
		self.email = fname+lname+'@aman.com'

	def get_details(self):
		print("The name is ",self.name)
		print("The email is ",self.email)

std1 = Student("Aman","Preet")
std1.get_details()

#that totally make sense init method is invoked by the creation of the object
#rest you can also check the pdf file as well.