Task 1-2. Only women older than 25 years old
import pandas as pd
df=pd.read_excel(r"C:\Users\dagii\Desktop\Homework\Homework #2\data.xlsx")
df.head()
#1
df.iloc[17, 3:6]
#2
df.loc[25:28,("firstName","age")]
#3
df.groupby("gender")['salary'].max()
df.groupby("gender")['salary'].min()
df.groupby("gender")['salary'].mean()
#4
import numpy as np
table = pd.pivot_table(df, values=['salary'], index=['gender'], aggfunc=np.mean)

