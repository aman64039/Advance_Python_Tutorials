"""
Parameter Ordering:
There is a order we have to follow or else things could break.So this will be the order In our function 
Declarations.
1.Parameters
2.*args
3.Default Parameters
4.**kwargs
If the function consist of all 4 of these we have to use this order.
"""
def display_info(a,b,*args,instructer="Aman",**kwargs):
	return [a , b, args , instructer , kwargs]

view = display_info(10,20,30,last_name="Preet",job="Instructer")

print(view)
#[10, 20, (30,), 'Aman', {'last_name': 'Preet', 'job': 'Instructer'}]
