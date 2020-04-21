#one way
def square(num):
	return num*num

print(square(9))

#2nd way
def square(num): return num*num

#syntax of lambda function
lambda num: num*num
#so this is the lambda which perform the same thing without the use of def and return keyword 
#lambda is a function which has no name, it just exist and we can store into a variable 
#in some of the articles its mentioned as ananomous function.
#this expression automatic return
square2 = lambda num : num*num
print(square2(9))
sum2 = lambda a,b : a+b
print(sum2(10,20))

print(square.__name__)	#square
print(square2.__name__) #<lambda>
print(sum2.__name__) #<lambda>

"""
The most comman use case is when you have some code that actually you need to pass the function
into another function as a parameter and that function will never used again.To proper undestand the 
concepts lets look of another conceot of GUI(Tkinter)
"""
#importing the tkinter library
import tkinter as tk
root = tk.Tk()
#creating a frame
frame = tk.Frame(root)
frame.pack()

#defining function to perform some functionallity
def say_hello():
	print("Hello")

#fitting 1 button on frame and on click say_hello function will be envoked
button = tk.Button(text="Click Me",command = say_hello)
button.pack()


#fitting second button on the frame 
button1 = tk.Button(text="Click Me2",command = lambda : print("Hey"))
button1.pack()
root.mainloop()