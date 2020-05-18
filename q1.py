#Create an inner function to calculate the addition in the following way

#Create an outer function that will accept two parameters ‘a’ and ‘b’ 

#Create an inner function inside an outer function that will calculate the addition of ‘a’ and ‘b’ 

#At last, an outer function will add 5 into addition and return it




def outer(x , y):
	sqr=x**2
	def inner(x , y):
		return x + y
	add = inner(x , y)
	return add + 5
	
a = float(input('enter the first number : '))
b = float(input('enter the second number : '))
finalAns= outer(a , b)
print('Final answer is : ' , finalAns)