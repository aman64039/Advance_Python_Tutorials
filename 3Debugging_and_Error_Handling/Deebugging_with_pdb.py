"""
When We Encounter an error in our code that is not intentional.So we didnt raise it, we didnt expect it.
or we can say that a silent error or silent bug like we can say our code isnt wotking the 
way we expect.but its not actually breaking the code.So thats the most frustrating.
the code didnt break but it result some diffrent result.
The tool i am going to introduce called pdb will actually help us understand our code and 
step through it to figure out where we are going wrong.
So pdb Stand for Python Debugger.Its a module which make sense when we want to use it we have to import it.
After importing there is a single method which will pause execuation of our code.
its name as pdb.set_trace()
That whatever we put it in our code on line 1 or on line 100.
when python encounter this line it will pause.
So it dosent quit dosent skip everything else it pauses and then in our terminal we can go and
intract with value or we can step through one line at a time.
Lets have a look on example:

"""
first = "First"
second = "Second"
result = first+second
third = "Third"
result = result+third
print(result)
#perfectly work

#but lets look how pdb will work in this.
import pdb
#wherever your code is breaking or you are facing difficulties to understand what is 
#going on the code so at that poiunt we hace to call a fucntion 
first = "First"
pdb.set_trace()
second = "Second"
result = first+second
third = "Third"
result = result+third
print(result)

"""
From the line where the function set_trace is called a new shell will be started
named as pdb and with the help n charcter we can execute the next and next line to check
what is going to happen.
#l --> list
#n --> next line
#p --> print 
#c --> continue (finish debugger)
#a --> all values
"""

#Lets have a look on another example
def add_number(a,b,c,d):
	#one way of importing
	#import pdb; pdb.set_trace()
	
	#second way
	#import pdb pdb.set_trace()

	#third way
	import pdb
	pdb.set_trace()

	return a+b+c+d
add_number(1,2,3,4)

