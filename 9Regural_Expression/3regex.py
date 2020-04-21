import re
def parse_name(input):
	name_Regex = re.compile(r'^(Mr\.|Mrs\.|Mrs\.|Mdme\.) ([A-Za-z]+) ([A-Za-z]+)$')
	matches = name_Regex.search(input)
#but what if i want to get only first name so as its discussed we had mention method
#name as groups and indexing of group so lets implement it
	print(matches.group(2))
	#will work perfectly

#Another Way
def parse_name1(input):
	#just i am provifing a name to the group as first and that is the syntax ?P<name>
	name_Regex = re.compile(r'^(Mr\.|Mrs\.|Mrs\.|Mdme\.) (?P<first>[A-Za-z]+) ([A-Za-z]+)$')
	matches = name_Regex.search(input)
#but what if i want to get only first name so as its discussed we had mention method
#name as groups and indexing of group so lets implement it
	print(matches.group('first'))
	#will work perfectly

parse_name("Mr. Amanpreet Singh")
print("\n")
parse_name1("Mr. Amanpreet Singh")
