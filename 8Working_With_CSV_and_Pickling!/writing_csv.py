"""
Writig to CSV File: We can write a csv file by 2 Diffrent ways Either using a lits of Either Using a Dict.
Way using List:
=============
Writing to CSV file using List: we have2 function name as Writer and writerow in CSV modules.
writer - creates a writer object for writing to csv.
writerow - function on write to write a row to the csv 

Another way of writing data using Dictionaries:
=============================================
DictWriter - creates a write object for writing using dictionaries.
fieldnames - kwags for DictWriter specifiying headers
writeheader - method on a write to write header row
writerow - method on a writer to write a row based on dictionary.

"""
from csv import writer , reader
with open("new.csv",'w') as f:
	csv_writer = writer(f)
	csv_writer.writerow(["Name",'Language'])
	csv_writer.writerow(["Aman",'Python'])

#Another Example:
#reading a file make some changes and updated data will store into a new file 
#one way using nested with statement
with open("newcsv.csv") as f:
	csv_reader = reader(f)
	with open("new.csv",'w') as f:
		csv_writer = writer(f)
		for i in csv_reader:
			csv_writer.writerow(i)

#Another way with only one file open at a time
with open("newcsv.csv") as f:
	csv_reader = reader(f)
	#data coverted into list and saved to a variabe
	data = [[s.upper() for s in row] for row in csv_reader]

with open("new.csv",'w') as f:
		csv_writer = writer(f)
		for i in data:
			csv_writer.writerow(i)


#Using Another way of writing the data into csv using Dictionary'
from csv import DictWriter
with open("abc.csv",'w') as f:
	headers = ["Name","Age"]
	csv_writer = DictWriter(f, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({"Name":"39"})












