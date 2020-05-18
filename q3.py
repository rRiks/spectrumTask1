#Given a Python list, remove all the even number from the list and save those even number in another list and print both the lists.



List1 = [1,2,3,4,5,6,7]
evenNum = [ ]
for num in List1:
	if (num%2==0) :
		evenNum.append(num)
		List1.remove(num)
print('List1:' ,List1)
print('List2:' ,evenNum)
		
			
		