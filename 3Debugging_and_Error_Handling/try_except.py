"""Handle Error
In Python , its is strongly encourged to use try/except blocks to catch exceptions when we can do
something about them.Lets See what will be the syntax.
try:
	action_to_be_performed 
except:
	there is an issue in so this except case is executing
"""
try:
	action_to_be_performed
except:
	print("Problem")
#except part will be executed because the string or name we had written is  not in " " or nothing like 
#a varaible
#every error is catched by except we can print whatever we want to print or lets see what will be happen
"""
If we know the error such as it is an NameError and we are catching a KeyError in that case
except case will not work
lets see 

dic = {'name':'Aman'}
try:
	d['name']
	#NameError will be there because d is not defined our dict is named as dic
except NameError:
	print("We have an issue ")
#perfectly Work

but lets see another case
try:
	dic['city']
	#KeyError will be there because city is not availble in our dictionary
except NameError:
	print("We have an issue")
#in this case error is not so handled it will raise an error name as key error

"""