import statistics
import pandas as pd
df = pd.read_csv('train.csv', header='infer')

import numpy as np
print(df.head(7))
df.info()
print(df.shape)
print(df.describe())

#Copying the File
df1 = df.copy()
df2 = df.copy()
df3 = df.copy()
df4 = df.copy()
df5 = df.copy()

df1 = df1.dropna(axis=0)
print(df1.shape)
print(df.shape)

df2 = df2.dropna(axis=1)
print(df2.shape)
print(df.shape)

#Replacing NA values with 21 in "Age" Column
df3.loc[df3.loc[:, "Age"].isna(), "Age"] = 21
df3.info()
#Checking Unique Available Data
df3.loc[:, "Cabin"].unique()

#Replacing NA in age with Mean
meanage = np.mean(df4.loc[~df4["Age"].isna(), "Age"].values) # type: ignore
print(meanage)
df4.loc[df4.loc[:, "Age"].isna(), "Age"] = meanage

#Replacing NA in Cabin with Most Frequent
mfcabin = statistics.mode(df4.loc[~df4["Cabin"].isna(), "Cabin"].values)
print(mfcabin)
df4.loc[df4.loc[:, "Cabin"].isna(), "Cabin"] = mfcabin

#Replacing NA in Embarked with Mode
mfembarked = statistics.mode(df4.loc[~df4["Embarked"].isna(), "Embarked"].values)
print(mfembarked)
df4.loc[df4.loc[:, "Embarked"].isna(), "Embarked"] = mfembarked

# Replacing NA in Age (Of those who didn't survive) with Mean
meanage0 = np.mean(df5.loc[(~df5["Age"].isna()) & (df5["Survived"] == 0), "Age"].values) # type: ignore
print(meanage0)
df5.loc[(df5["Age"].isna()) & (df5["Survived"] == 0), "Age"] = meanage0

# Replacing NA in Age (Of those who survived) with Mean
meanage1 = np.mean(df5.loc[(~df5["Age"].isna()) & (df5["Survived"] == 1), "Age"].values) # type: ignore
print(meanage1)
df5.loc[(df5["Age"].isna()) & (df5["Survived"] == 1), "Age"] = meanage1