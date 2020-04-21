#errr int('')

try:
	num = int(input("Please enter the number "))
except:
	print("Thats not a number ")
#work perfectly

#another use 
try:
	num = int(input("Please enter the number "))
except:
	print("Thats not a number ")
else:
	print("This is else")
#in this case if we are passing a valid number our else part will be executed


#Another example
try:
	num = int(input("Please enter the number "))
except:
	print("Thats not a number ")
else:
	print("This is else")
finally:
	print("This is Finall case")
#either the except work or wither else finally will work for sure at the lasy
#most often try and except is used but you have to know this keyword as well.



#Another Example
num1 = int(input("Please enter the first number ")) #10
num2 = int(input("Please enter the first number ")) #2
try:
	result = num1/num2
	print(result)
except:
	print("Soemthing went wrong")


#Anoter case 
num1 = int(input("Please enter the first number ")) #10
num2 = int(input("Please enter the first number ")) #0
try:
	result = num1/num2
	print(result)
except Exception as E:
	print(E)
	#what every will be error will be printed

#Another Example
num1 = int(input("Please enter the first number ")) #10
num2 = int(input("Please enter the first number ")) #a
try:
	result = num1/num2
	print(result)
except ZeroDivisionError:
	print("Can be divide by 0")
	#what every will be error will be printed
except TypeError:
	print("Type should br true")
else:
	print(f"{num1} divided by {num2} is ",result)



#Another Example
num1 = int(input("Please enter the first number ")) #10
num2 = int(input("Please enter the first number ")) #a
try:
	result = num1/num2
	print(result)
except (ZeroDivisionError,TypeError) as e:
	print(e)
	#what every will be error will be printed
except TypeError:
	print("Type should br true")
else:
	print(f"{num1} divided by {num2} is ",result)

