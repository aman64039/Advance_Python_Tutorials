"""
Genrators are the iterators(Its a subset of iterator but thing to remember not an iterator is
a genrator).
Genrators can be created with genrator Function.
Generator function is responsible to genrate a sequance of values.
Internally Genrator function uses yield keyword.

Regural Function: 1.It uses Return.
2.Return Once
3.When invoked returns the return value

Genrators Fucntion: 1.It uses Yield.
2.Can Yield Multiple Times
3.When Invoked , return a genrators 

#lets have a look
"""
def count_up_to(max):
	count = 1
	while count<=max:
		yield count
		count+=1

counter = count_up_to(10)
while True:
	print(next(counter))
#will retun a genrator objects
help(counter) #you will get the list of method so you can check next will be there.

#lets implement a for loop on genrator object
for i in counter:
	print(i)
#for loop automatically called or invoke next() method.
g = (x for i in range(20))
#another way


#to genrate first n number
def firstn(num):
	n= 1
	while n<=num:
		yield n
		n+=1

for i in firstn(20):
	print(i)



#to genrate fibonacci numbers (0,1,1,2,5,8,13,.......)
def fab(n):
	a,b,c = 0,1,0
	while c<=n:
		yield a
		a,b = b,a+b
		c+=1
for i in fab(100):
	print(i)


"""
Advantages of Genrators:
1.Perfromance will be imporoved.
2.Memory Utilization will be imporved
"""
from random import choice
import time
names = ['sunny','bunny','munny','cunny']
subjects = ["Python","Java","Blockchain"]

def people_list(num):
	result = []
	for i in range(num):
		person = {"id":i,
				'name':choice(names),
				'subject':choice(subjects)}
		result.append(person)
	return result

start = time.clock()
people = people_list(10000000)
end = time.clock()
print("Time taken by list",end - start)


#genrator
def people_genrator(num):
	result = []
	for i in range(num):
		person = {"id":i,
				'name':choice(names),
				'subject':choice(subjects)}
		result.append(person)
	yield result

start = time.clock()
people = people_genrator(10000000)
end = time.clock()
print("Time taken by Genrator",end - start)
