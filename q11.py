#Write a Pandas program to count the duplicate rows of diamonds DataFrame.


import pandas as pd
data = pd.read_csv('https://github.com/rRiks/spectrumCet/blob/master/diamonds.csv?raw=true')

print("Given Dataframe size is : ")
print(data.shape)
print("\n Duplicate rows of diamonds DataFrame:")
print(data.duplicated().sum())

