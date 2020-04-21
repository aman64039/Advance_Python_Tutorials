"""
As we know we have attributes in classes which represent the behaviour or just providing details of the object.
We have 2 types of attributes named as class attributes and instance attributes.
Class Attributes:These are the attributes which are same to all the instances of the class, that means
for every object of the class which you create the value of class attribute will remian same.
You can check the follwing example 
"""
class Employee:
	#class attributes
	noOfWorkingHours = 40

emp1 = Employee()
emp2 = Employee()
print(emp1.noOfWorkingHours)
print(emp1.noOfWorkingHours)

#changing the value of the class attribute for each and every objects
Employee.noOfWorkingHours = 45

print(emp1.noOfWorkingHours)
print(emp1.noOfWorkingHours)



"""Here you can see that the no of working hours of each and every employee should remain same
so we have used it as a class attribues where as name and other parameters vary on objects.
I am also defining very much fine concept where you will got the concepts of another type of attribute
"""
#One way to initlize the instance attribute
emp1.name = "Aman"
emp2.name = "Preet"

print(emp1.name)
print(emp1.name)

#creating a new instance attribute name as noOfWorkingHours
emp2.noOfWorkingHours = 40

print(emp1.noOfWorkingHours)
print(emp1.noOfWorkingHours)
"""
Note:You did not actually change the value of class attribute here you are creating a new instance 
attribute of object emp1 with the same name as a class attribue.
So how python acces the attribute is it first check is there any instance attributes avaible of that name 
if it found iy will print otherwise if its not found then its going to find in class attributes.
In our this example i am uisng something emp1.noOfWorkingHours so this is also an instance attribute so 
it will return 40 but on emp2.noOfWorkingHours this is not a instance attribute so it will print the 
value of the class attribute 
"""
#check this example as well
emp1.age = 39
print(emp1.age)
print(emp2.age)



