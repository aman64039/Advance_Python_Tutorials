"""
Read the data from the existing file.
You can read a file with the open Function.
Open return a file object to you.
You can read the a file object with the read method.
The default mode of open function is read that means it will read the file onlt if we are not 
providing the mode in open function
There are some of the default parameter availble in open function but we have to pass the file name
as the arguemnt.
"""
data = open("file.txt")
content = data.read()
print(content)

print("=====================")
#again the reading the data
print(data.read())
#nothing is printing so lets discuss why so
"""
Cursor Movement
==============
Python reads files by using cursor.
This is like the cursor you see when you're typing.
After reading the file the curser is at the end.
To move the cursor , use the seek method.
"""
print("After seek\n")
data.seek(0)
#move the cursor at begning
print(data.read())
print("After seek\n")
data.seek(10)
#move the cursor at 10th
print(data.read())

#Another method that is readline
data.seek(0)
print(data.readline())
print(data.readline())

#readlines will return the list of the lines
data.seek(0)
print(data.readlines())

#get the name of the file 
print(data.name)

#will return True if the file is closed otherwise false 
print(data.closed)

"""
closing a file:
you can close a file using close method.
you can check if a file is closed with the closed attributed as discussed.
once 
"""
data.close()
print(data.closed)
print(data.read())
#error because now file is closed