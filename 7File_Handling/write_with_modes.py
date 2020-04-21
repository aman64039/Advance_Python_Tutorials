"""
option1:
file = open("file.txt")
file.read()
file.close()
fie.closed

option2:
with open("file.txt") as file :
	file.read()

file.closed()

#the advantage of using with statement that it will automatically
close the file. there is no need to invoke a close method.
"""
with open("file.txt") as file:
	data = file.read()

print(data)
print(file.closed)

"""
Writing the file:
You can also use open to write a file.
Need to specify the 'w' flag as the second argument to the parameter name as mode.
with open("file.txt",'w') as file:
	file.write("My name is Amanpreet Singh.")
	file.write("I am a Data Science Trainer.")
"""
with open("file.txt",'w') as file:
	file.write("My name is Amanpreet singh")
"""
Points to Note.
If the file is not availble which you are opening with open function and passing 'w' mode the file 
will be created.
If the file is availble and if you wanna write something in that with the help of write function.
The content which is already availble in file will be removed and new content will be wriitten.
Basically overwritten will be there.
"""

#Modes of opening the file.
"""
We have many of the modes by which we can open a file but most commanly used are the three which i am 
going to discuss.For the other modes you can go to the docs. 
https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

r - Read a file(no writing) - this is the default in open function.
w - write to a file(previous contents removed)
a - append to a file(previsous contents not removed) 
r+ - Read and write to a file (writing based on cursor)
"""
with open('file.txt','a') as file:
	file.write("Appending the content in the file\n")
	file.write("And this will not remove the last content from the file")

#if you want to add something at the starting point.
with open('file.txt','a') as file:
	file.seek(0)
	file.write("Appending the content in the file\n")

#using r+ mode by which you will be able to write and read as well
#writing
with open('file.txt','r+') as file:
	file.write("My name is Amanpreet.")

#reading
with open('file.txt','r+') as file:
	file.read()