#Get the key corresponding to the minimum value from the following dictionary using appropriate python logic.




def minimums(givenDictionary):
    positions = []
    min_value = float("inf")
    for k, v in givenDictionary.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            positions = []
            positions.append(k)
    return positions

sample = {'physics' : 88 ,  'maths' : 75 ,  'chemistry' : 72 , 'Basic electrical' : 89 }

minKey = minimums(sample)
print('The minimum valued key in the dictionary is : ' ,minKey)