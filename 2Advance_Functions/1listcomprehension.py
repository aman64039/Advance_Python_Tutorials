#lest see an example to understand the concept
#if i want to multiple all the element of list by 2 and store it into a new list
#one way
num = [1,2,3,4,5,6,7,8,9,10]
dl = []
for i in num:
	dl.append(i*2)
print(dl)
#2nd way
dl1 = [x*2 for x in num]
#so what it will do is for every x in num are going to multiply by 2 and put it into a new list
#this is a syntax of list comprehension
print(dl)

#Another example for Charcter
name = "Amanpreet Singh"
upername = [char.upper() for char in name] 
#['A','M','A','N'.........]
print(upername)

#we can do with ranges as well
a = [i*2 for i in range(1,10)]
print(a)


#conditional logic to list comprehension
number = [1,2,3,4,5,6,7,8,9,10]

#get even and odd list comprehension
odd = [i for i in number if i%2!=0]
even = [i for i in number if i%2==0]
print(even)
print(odd)

#else in lisr comprehension
#multiple number by 2 if its even otherwise it wil divide by 2
cd = [i*2 if i%2==0 else i/2 for i in number]
print(cd)
