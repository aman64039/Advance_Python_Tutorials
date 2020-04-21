"""
Similar to Map we can pass a function and then an iterable collection. 
Filter allows the same but the work some how diffrently.
Filter does what ist sounds like it allows us to tale a collection and filter out particular 
item that we want based off an expression or condition.
Return the filter object and we can further convert into any data structer.
The object contain only the values that return true to the lambda.So lets have a look
"""
#get the list of even numbers 
l = [1,2,3,4,5,5,6,7,8,9,10]

#with loop
el = []
for i in l:
	if i %2==0:
		el.append(i)
print(el)

#lets have a look on filter
fl = list(filter(lambda x : x%2==0,l))
print(fl)

#Another example
names = ['austin','penny','anthony','angel','billy']
a_names = list(filter(lambda n: n[0]=='a',names))
print(a_names)


#Another example
users = [{"username":"samuel","tweets":['I love Cake','I love Pie']},
{"username":"katie","tweets":['I love my dog']},
{"username":"jeff","tweets":[]},
{"username":"bob123","tweets":[]},
{"username":"dogoo_luvr","tweets":['Dogs are the best']},
{"username":"guitar_gal","tweets":[]}]
#i want to filteout that user who never tweeted

#one way
def test(detail):
	if(len(detail['tweets'])<1):
		print(detail['username'])
		return detail['username']

list_user = list(filter(test,users))
print(list_user)


#2nd way 
list_user = list(filter(lambda x: len(x['tweets'])==0 , users))
print(list_user)

#Return the user who are active beacasue x['tweets'] is true because its consist of some values
list_user = list(filter(lambda x: x['tweets'],users))
print(list_user)

#return unactive users
list_user = list(filter(lambda x: not x['tweets'],users))
print(list_user)




#combining Filter and Map
names = ['Vikram' , 'Aman' , 'Deep']
#i want ti retrun a new list with string your instructer is + each_value in the given list
#but only if the value is less than 5 chracter

instructer = list(map(lambda name: f"You instructer is {name}",filter(lambda value: len(value)<5 ,names)))
print(instructer)
#so in this case our filter will run first which create a list of names whose value is less than 5 char.




#so again taking the last example of inactive user
list_user = list(map(lambda user : user['username'].upper(),filter(lambda x: not x['tweets'],users)))
print(list_user)
#so it will return just the username of the inactive users

#Note :
# Instead of these list comprehension which is avialble in python is most offten used 
# but as its in the conctent so we have to know this stuff as well.
