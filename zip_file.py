import os
#zipfile is a built-in Python module used to work with .zip compressed files — without needing any external library.
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

#loading and exploring the dataset
df=pd.read_csv(r"C:\Users\mruna\Desktop\InfosysInternship\Indian_Traffic_Violations.csv")
# print(df.tail())

#print(df.info()) #info about col type and not null count
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.shape) #total rows n cols
# print(df.dtypes)

#MOST COMMON VIOLATION TYPES
# plot = plt.figure(figsize=(12,6))

# sns.countplot(
#   y = df['Violation_Type'],
#   order = df['Violation_Type'].value_counts().index, #desc sorted
#   palette = 'coolwarm' 
# )
# plt.title("Most common violation type")
# plt.xlabel("count")
# plt.ylabel("Violation type")
# plt.tight_layout() #prevents lavel cutoff
# plt.show()

# top5 = df['Violation_Type'].value_counts().head(5)
# print("Top 5 Violation Types:\n")
# print(top5)

#distribution of fine amounts hist+kde
plot = plt.figure(figsize=(10,5))
sns.histplot(data=df ,x = "Fine_Amount", bins=30, kde=True)
plt.title("Distribution of fine amounts histogram")
plt.xlim(0, df['Fine_Amount'].quantile(0.99))
# plt.show()

#Show sumary states and show mean median

summary_state = df["Fine_Amount"].describe()
print("Summary states of data")
print(summary_state)

#median
median_amts = df["Fine_Amount"].median()
mean_amt = df["Fine_Amount"].mean()
print("median"  , median_amts)
print("mean" , mean_amt)

