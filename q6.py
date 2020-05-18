#Program to create simple calculator in Python which on input of 1,2,3,4 should add , subtract , multiply and divide respectively.




def addition(a , b):
	return a + b

def subtraction(a , b):
	return a - b

def multiplication(a , b):
	return a * b

def division(a , b):
	return a / b

print('select an operation :')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')


while True:
	choice = input('enter operation type(1 or 2 or 3 or 4 ) : ')
	
	if choice in ('1' , '2' , '3' , '4'):
		n1 = float(input('enter the first number : '))
		n2 = float(input('enter the second number : '))
		
		if choice == '1' :
			print(n1 , '+' , n2 , ' = ' ,addition(n1,n2))
			
		elif choice == '2' :
			print(n1 , '-' , n2 ,' = ' ,subtraction(n1 , n2))
			
		elif choice == '3' :
			print(n1 , '*' , n2 , ' = ' ,multiplication(n1 , n2))
			
		elif choice == '4' :
			print(n1 , '/' , n2 , ' = ' ,division(n1 , n2))
			
	else:
		print('invalid choice')