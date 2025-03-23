import pandas as pd

df = pd.read_csv('data001.csv')

#平均
mean1 = df.groupby('担当者').mean()

#最大値
max1 = df.groupby('担当者').max()

#最小値
min1 = df.groupby('担当者').min()

#合計
sum1 = df.groupby('担当者').sum()

#回数
count1 = df.groupby('担当者').count()


print mean1

