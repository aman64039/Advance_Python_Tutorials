"""
Every Thing in Python is Object
Before Starting the concept of classes and object lets have a idea why its needed.Lets suppose you are definig 
a function name as calculate_Salary which is going to calculate the salary which can be called by an employee
to calculate the salary of that but in normal program this function can be called on student as well 
which dosent make any sense and we want to restrict this function only to an employee not to a student.
So classes help us to do that by placing this function into a block and seal it and make it availble for
only employee not to a student. 
So now lets discuss what are classes and Objects.
BY the Defination the classes are logical collection of attributes and methods.
and object is instance of a class.
Lets try to understand the concept of classes and objects.
Suppose we have a something as a Human and human has name , age , gender and human can perform some task 
like he can walk , he can eat and so on. In the same we if i am relating the human to a classes and object 
A human will be a class which consit of some attributes such as name , age and some method that 
he can walk , eat and i , you all we all are the objects of human class.
The process of creation of an object of a class is called
instantiation

so when you are just starting with object oriented programming concept there are 3 things to identify
that is 
Noun -------------------------------------------> A class 
Adjective(Properties which define the noun) ----> Attributes
Verbs(Action performed by your noun) -----------> Methods

"""
#Implementation of the classes and object
#here we are creating a class name as an Employee by convention the first letter of the class
#should be in upper case
#class name that is noun 
class Employee:
	#class variable or attributes 
	name = "Amanpreet Singh"
	profile = "Python"

#creating object1
emp1 = Employee()
#Object 2
emp2 = Employee()

#getting the name of employee1
print(emp1.name)
#getting the name of emplyee2
print(emp2.name)
#initlizing the name of emplyee2
emp2.name = "Preet Singh"
"""
This is not a right way to initlize the attributes of the object when we have attribute which is
specific to each object the way is diffrent and we have special method to that.In our next file 
you are going to dicuss the methods ,attributes and Special method as well.
As on the top i had metion that each and every thing is an object.So what this mean
check the follwing example
"""
number = [10,20,30,40]
print(type(number)) #return <class list>
#so what is happend there number is a object of list class.
#So at the end we discussed that class is a blue print and object is execution of that blueprint 