"""Hiding the implementation details from the end user is called as encapsulation
Abstraction is the process of steps followed to achieve encapsulation

Lets take an example you are driving a car and you want to stop it. As the driver of the car the only thing
you need to awair of to apply the break you dont need to know whats happen internally When you apply the break
Applying Breake is the layer of abstraction that has been provided to you and What happen internally
has been encapsulated, that is hidden to your view.
Now in programming you have been using both all along though you are not aware of it 
The method thats you create which an object calls upon those are the layer of the abstraction which
you provide to user and in your class when you write the statement of method that is encapsulation being done
.Encapsulation is perform to achive abstraction.It is a process of hiding the implementation detail from 
the user.
Lets take an example which we have used a lot.
While using a list we have a method name as append which is going to adding the element at the last.
So at here append is the layer of the abstaction that is provided to you dont know the internal implementation
of the append operation which is encapsulated in list class
So lets implement the example which providing layer of Abstraction and achiving it by Encapsulation.

Implement the Library Management System which handle the follwing task
1.Customer should be able to display all the bookd availble in library.
2.Handle the process when a customer request to borrow a book.
3.Update the library collection when the customer returns a book
"""
 



class Library:
	def __init__(self,listofbooks):
		self.availblebooks = listofbooks
	def showbooks(self):
		print("Availble Books")
		for i in self.availblebooks:
			print(i)
	def lendbook(self,requestedBook):
		if requestedbook in self.availblebooks:
			print("Hey you lended a book name as ",requestedBook)
			self.availblebooks.remove(requestedBook)
		else:
			print("This book is not availble ")

	def addbook(self,returnedBook):
		self.availblebooks.append(returnedBook)
		print("Done")



class customer:
	def requestbook(self):
		book = input("Please enter the name of the book you want ")
		return book

	def returnbook(self):
		book = input("Please enter the name you want to return ")
		return book


library = Library(['Who Will Cry When You Die','Think and Grow Rich','For One More Day'])
customer = Customer()

while True:
	print("Enter 1 to display the avaible books.")
	print("Enter 2 to request a book.")
	print("Enter 3 to return a book.")
	print("Enter 4 to exit")
	a = input()
	if(a=='1'):
		library.showbooks()
	elif(a=='2'):
		requestedbook = customer.requestbook()
		library.requestbook(requestedbook)
	elif(a=='3'):
		returnedbook = customer.returnbook()
		library.addbook(returnedbook)
		
	elif(a=='4'):
		exit()

"""
Similar to a library management system, write a program to
provide layers of abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are
being provided for rent
2. Cost per day:
Hatchback - $30
Sedan
- $50
SUV
- $100
3. Give a prompt to the customer asking him the type of car
and the number of days he would like to borrow and provide the
fare details to the user."""
class Car:
    def __init__(self):
        # A dictionary to map the type of car and price per day
        self.carFare = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}

    def displayFareDetails(self):
        print("Cost per day: ")
        print("Hatchback: $",self.carFare['Hatchback'])
        print("Sedan: $", self.carFare['Sedan'])
        print("SUV: $", self.carFare['SUV'])

    def calculateFare(self, typeOfCar, numberOfDays):
        # Calculate the fare depending upon the type of car and number of days as requested by the user
        return self.carFare[typeOfCar] * numberOfDays


car = Car()
while True:
    print("Enter 1 to display the fare details")
    print("Enter 2 to rent a car")
    print("Enter 3 to exit")
    userChoice = (int(input()))
    if userChoice is 1:
        car.displayFareDetails()
    elif userChoice is 2:
        print("Enter the type of car you would like to borrow")
        typeOfCar = input()
        print("Enter the number of days you would like to borrow the car")
        numberOfDays = int(input())
        fare = car.calculateFare(typeOfCar, numberOfDays)
        print("Total payable amount: $",fare)
        print("Thank you!")
    elif userChoice is 3:
        exit()