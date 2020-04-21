#in this tutorials i will show how to use re module and builtin methods to build some 
#simple functions

import re

def extract_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

def is_valid_phone(input):
	#starting with 3 numbers and ending with 4 number
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	return False

print(extract_phone("My number is 432 567-8523"))
print(extract_phone("My number is 432 567-852333"))
print(extract_phone("My number is 432 567-8523555"))
#this will work either its not a fine pattre
#so lets make me some of the changes in the regex pattren

def extract_phone1(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

print(extract_phone1("My number is 432 567-8523"))
print(extract_phone1("My number is 432 567-852333"))
print(extract_phone1("My number is 432 567-8523555"))

#another way of valid phone isneatd of ^ and $ we can use a method name as fullmatch
def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

print("================================================")
#url regex
a = 'https?://www.[A-Za-z-]{2,256}\.[a-z]{2,6}[-a-zA-Z0-9@:%_\+.~#?&//=]*'
b= 'http://www.youtube.com/videos/asd/das/asd'
#so lets discuss with the examle of this
"""
http://www.youtube.com/videos/asd/das/asd
so lets split the regex for this example

https? -- http
://www. -- ://www.
[A-Za-z]{2,256} -- youtube
.[a-z]{2,6} ---   .com
[-a-zA-Z0-9@:%_\+.~#?&//=]*' ---- videos/asd/das/asd
"""
url_pattren = re.compile(a)
match = url_pattren.search(b)
if match:
	print(match.group())   #will print the matched result

#another example
a = '(https?)://(www.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
b= 'http://www.youtube.com/videos/asd/das/asd'
url_pattren = re.compile(a)
match = url_pattren.search(b)
if match:
	print(match.groups()) #will print the tuple which consist of groups
	#('http', 'www.youtube.com', '/videos/asd/das/asd')

#Another concept
print(match.group(0))
print(f"Protocol: ",match.group(1))
print(f"Domain: ",match.group(2))
print(f"another stuff: ",match.group(3))
