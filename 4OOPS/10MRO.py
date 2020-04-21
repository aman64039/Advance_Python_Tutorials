"""
In our this example we are going to discuss the diamond shape problem

  A
 / \
B   C
 \ /
  D
Class B and Class C is inhert from class A and Class D is inhert from Class B and Class A.
So Class D inherting the feature of all the claases here A,B,C

"""
#Case1:Method will not be overridden in class B and C.
class A:
	def method(self):
		print("This is a method of class A")
class B(A):
	pass
class C(A):
	pass
class D(B,C):
	pass

d = D()
d.method()
#the method which is in class A will be executed here

#case 2:Method will overridden to class B but not in class C.
class A:
	def method(self):
		print("This is a method of class A")
class B(A):
	def method(self):
		print("This is a method of class B")
class C(A):
	pass
class D(B,C):
	pass

d = D()
d.method()
#in this case the method which is mentioned in class be will be invoked


#case 3:Method will be overridden in class C and not in class B.
class A:
	def method(self):
		print("This is a method of class A")
class B(A):
	pass
class C(A):
	def method(self):
		print("This is a method of class C")
class D(B,C):
	pass

d = D()
d.method()
#In this case again the method of class C as its overridden in class C.



#case 4:Method will be overridden in both class B and C.
class A:
	def method(self):
		print("This is a method of class A")
class B(A):
	def method(self):
		print("This is a method of class B")
class C(A):
	def method(self):
		print("This is a method of class C")
class D(B,C):
	pass

d = D()
d.method()

"""In this case the method of class B is will be invoked.The method resoulution depend upon the order
in which you inherit the derived class.which mean if you have class B first so method which is overrideden will be 
execute. This is called Method Resolution Order.

"""
