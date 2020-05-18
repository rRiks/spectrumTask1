#Write a Pandas program to calculate count, minimum, maximum price for each cut of diamond DataFrame.



import pandas as pd
data = pd.read_csv('https://github.com/rRiks/spectrumCet/blob/master/diamonds.csv?raw=true')

print("\n Count, minimum, maximum  price for each cut of diamond DataFrame : \n")

print(data.groupby('cut').price.agg(['count', 'min', 'max']))