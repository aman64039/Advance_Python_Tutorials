"""regular Expression in Python:
Now we are going to write the code that will match the string using a given regular
expression or define a function which retrun true if something matches a pattern.
We have a module name as re to perform regular expression.
"""
#import regex module
import re

#define our phone number regex
pattren = re.compile(r'\d{3} \d{3}-\d{4}')

#search our string with our regex
#implementation of search on re object that is one way that is we create a
#regex object first we complie it and then we are applying search on it.
res = pattren.search("Call me at 415 555-4242")
res1 = pattren.search("Call me at 415 555-4242 or 310 234 9999")

#will print out the first matchAcc to docs of re 
#search scan through string looking for the first location where the re pattren produce
#a match so it dosent support finding more than one match
print(res.group())
print(res1.group())

#if we want to get all the matches instead of search we have to use findall method
res2 = pattren.findall("Call me at 415 555-4242 or 310 234-9999")
print(res2)
#findall return the all the matches

#second way to use the search without compiling regex
#re.search(pattren_of_re , string)
res3 = re.search(r'\d{3} \d{3}-\d{4}' , "Call me at 415 555-4242")
print(res3.group())

#but the better way and most comman used is that we have to compile the regex first