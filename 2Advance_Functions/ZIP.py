"""
zip:Make an iterator that aggregate element from each of the iterables.
Return an iterator of tuples.
Lets have a use case of zip.
we have a 2 list of the same length and if we are applying zip it will make a new list where it pairs
up the first two numbers from the list and then the second.
"""
zp = zip([10,20,30],[40,50,60])
ls = list(zp)
print(ls)
#return [(10,40),(20,50),(30,60)]

for i in zip([10,20,30],[50,60,70]):
	print(i)

#unpacking of zip
ls_zp = [(10,40),(20,50),(30,60)]

ls = list(zip(*ls_zp))
print(ls)