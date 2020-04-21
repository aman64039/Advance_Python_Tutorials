"""
*args:-A special Operater we can pass to a fucntion that gathers remaining arguments as a Tuple.
This is just a parameter you can call it whatevery you want as long as its starts with *.I will show you some other
names you could use but the standard name is *args.
So what has to be there is * and then what come after args is conventional but we can talk other options.
So what it dose we have a function defination if wer put *args as a parameter it will collect any 
number of additional or extra arguments that have been passed in into a single parameter called args or 
what ever we name this.


"""

def sum_all(num1,num2,num3):
	return num1+num2+num3

print(sum_all(4,5,6))
#but what if i am calling the function in this way sum_all(10,20,30,40,50,60,70,80)
#error will be there.

#case1
def sum_all(*args):
	#args is a tuple
	print(args)

sum_all(1,20,30,40,50)

#case2
def sum_all(*args):
	return sum(args)

print(sum_all(10,20,30,40,50,60,90,90))


#case3
def sum_all(a,b,c,*args):
	print(args)

sum_all(10,20,30,40,5,6,90)
#will print (40,5,6,90)


#case4
def sum_all(*a):
	print(a)

sum_all(10,20,30,40,50,60)
#args is just a standard name instead of args you can use any name 



#Tuple unpacking
def sum_all(*args):
	total = 0
	for i in args:
		total +=i
	print(total)


a = [10,20,30,40,50]
b = tuple(a)

# sum_all(a)
#what if instead of values we are passing a list or tuple as a arguments 
#so the value or args will become ([10,20,30,40,50],) or ((10,20,30,40,50]),)
#and it will through me an error TypeError: unsupported operand type(s) for +=: 'int' and 'list'
#so in case we have to use * while calling as well

sum_all(*a)
#this is called as unpacking why so because we are unpacking the list or tuple into indevidual






