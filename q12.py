#Write a Pandas program to get sample 75% of the diamonds DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame



import pandas as pd
data = pd.read_csv('https://github.com/rRiks/spectrumCet/blob/master/diamonds.csv?raw=true')

print("Given Dataframe:")
print(data.shape)
print("\n After Sampling 75% of diamonds DataFrame's rows without replacement :\n ")
result = data.sample(frac=0.75)
print(result)
print("\nRemaining 25% of the rows :\n ")
print(data.loc[~data.index.isin(result.index), :])
