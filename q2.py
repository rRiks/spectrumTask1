#Given input String of combination of the lower and upper case ,arrange characters in such a way that all lowercase letters should come first.




inputStr=input('enter the given string : ')
words = inputStr.split()
lower = [ ]
upper = [ ]
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedStr= ''.join(lower + upper)
print("\n arranging characters as per question having lower characters first:")
print(sortedStr)