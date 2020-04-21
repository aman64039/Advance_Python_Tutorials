"""
As you know json is the most popular data format use to formating semi structer data.
It is used to stroe the information in easy and organized manner.
Data will be in text format when exchanging between server and browser
Why Json: 1.Json has a more compact style than xml, and its often more readable.
The lightweight approach of json can make significant imporvements
2.The Xml software parsing process can take long time.Json uses less data overall,so it reduce the cost
and increase the speed.
"""

import json
#Store information in str data type
people =""" {
	"people":[
	{
	"name":"Amanpreet",
	"emp_no":"1234",
	"emial":"abc@a.com"
	},
		{
	"name":"Preet",
	"emp_no":"12345",
	"emial":"abcd@a.com"
	}


	]
}"""

print(type(people))

#convert the json string to python dict or Json format
data = json.loads(people)
print(data)
print(type(data))

for i in data['people']:
	print(i['name'],i['emial'])

#second case that convert back python dict to python string.
new_string = json.dumps(data)
#it will dumps the data of dict to sring
print("\n")
print(new_string)
print(type(new_string))

"""
In our dumps fucntion we have some of the parameters such as 
sort_key which take argument in bool data type either true either flase
indent how much indent we want
separators by how the objects will be seprated such as items seprations and key value
"""
new = json.dumps(data, indent=4, separators=(". ", " = "),sort_key=True)
#the string will be sorted , indented by 4 items are seprated by '.' and key valuea re
#seprated by '='


#laod a json file in python
#deserlzation.
with open("file.json") as f:
	data = json.loads(f)


#serlization.
with open("newfile.json",'w') as f:
	json.dump(data,f)

