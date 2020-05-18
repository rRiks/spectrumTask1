#Write a Pandas program to select a series from diamonds DataFrame. Print the content of the series






import pandas as pd
data = pd.read_csv('https://github.com/rRiks/spectrumCet/blob/master/diamonds.csv?raw=true')

print (data['cut'])