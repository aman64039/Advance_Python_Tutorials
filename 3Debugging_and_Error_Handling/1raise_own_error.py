"""
Its a fact that we all make mistakes. it can be human error or syntax error.
sometime we are using database and the connectivity will being crashed.Which make sense error happens all 
the time. So how to fix that is really really important part of being a developer and the first step to
preventing them and fixing them is just understand them.
Some of the errors are 
Syntax error:- Occurs when Python encounter incorrect syntax.such as 
def first:
None = 1
return
def name((
2.Name Error:This occure when a variable or function not defined
3.Type Error:- An opertaer of function is applied on wrong type.

You can also raise you own error by using a raise keyword then error name and in paramthesis
description about the error


raise ValueError('Invalid value ')
raise ValueError
raise NameError(".........")

Lets have a look on example which define the raise very well
"""

def colorize(text,color):
	colors = ("red","black","blue")
	if type(color) or type(text) is not str:
		raise TypeError