#Write a Pandas program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame.


import pandas as pd

data = pd.read_csv('https://github.com/rRiks/spectrumCet/blob/master/diamonds.csv?raw=true')

print("Given dataframe:")

print("Number of rows and columns:")
print(data.shape)

valueMissingRow = data.dropna(how='any').shape

print("After droping those rows where values are missing the given dataframe will be : " , valueMissingRow)
