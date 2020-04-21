"""
all():-Return True if all the elements of the iterable are truthy(or if the iterable is empty)
lets take an example

any():- Return True if any element of the iterable is truthy. if the iterable is empty return false
"""
#return because all the vaues are true
print(all([1,2,3,4,5,6]))

#return false coz we have a 0 that is false
print(all([0,1,2,3,8]))

#another example
people = ['Charlie','Casey','Cody','Carly','Christina']
print(all([name[0]=='C' for name in people]))
#will return true because the condition is true for each and every name

#another example
people = ['Charlie','Casey','Cody','Carly','Aman']
print(all([name[0]=='C' for name in people]))
#will return False because one condition is not true



#Any
print("Any")
print(any([val for val in [1,2,3,4,5,6] if val >2]))