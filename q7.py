#Write a Pandas program to read a csv file from a specified source and print the first 5 rows



import pandas as pd
data = pd.read_csv('https://github.com/rRiks/spectrumCet/blob/master/diamonds.csv?raw=true')

print (data[0:5])