"""
CSV: Comma seprated value.The most popular data format.
We can read cvs file just like other text file.
Python has a built in csv module t read and write csvs more easily.
Its just a way of taking data usually tabular data and just sticking it in a file and storing it.
So that we can do something with that later.
"""
#one way:
with open("employees.csv") as f:
	data = f.read()
print(data)

"""
Secondly with the help of CSV module.
There are 2 diffrent way to read teh data in csv module
reader - lets you iterate over rows of the csv as a list
dictreader - lets you iterate over rows if the csv as OrderdDicts
"""

#reader:
from csv import reader
with open("employees.csv") as f:
	#csv reader is just a iterator so that we can use next function on it
	csv_reader = reader(f)
	next(csv_reader)
	#next is just to remove the header
	for row in csv_reader:
		print(row)
		break
#break is that so taht i just want to print 1 row only
print("\n")
#Another Example
with open("employees.csv") as f:
	csv_reader = reader(f)
	next(csv_reader)
	for row in csv_reader:
		print(f"{row[0]} belongs to {row[7]} team")
print("\n")

#dict reader
from csv import DictReader
with open("employees.csv") as f:
	csv_reader = DictReader(f)
	for row in csv_reader:
		print(row)
		#this will a orderd dict in python that merans with the help of key we can access the data
		break

# Another Example
with open("employees.csv") as f:
	csv_reader = DictReader(f)
	for row in csv_reader:
		print(row['First Name'])

#if we have  a data with some of the another delimiter so we have another paramerter name as
#delimiter in which we have to pass the delimiter as an argument to read the data in that way.

with open("employees.csv") as f:
	csv_reader = reader(f,delimiter="|")
	next(csv_reader)
	for row in csv_reader:
		print(f"{row[0]} belongs to {row[7]} team")
