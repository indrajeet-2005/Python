# Titanic Survival Analysis 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------- 
# Loading Dataset
# -----------------------------
print("Loading Titanic Dataset...\n")

df = pd.read_csv(r"D:\AI_ML_PYTHON\Advance python\final_project_1\data\titanic.csv")

print("First 5 Rows:")
print(df.head())



# -----------------------------
# Dataset information
# -----------------------------
print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())



# -----------------------------
# data cleaning and filling some value
# -----------------------------
print("\nCleaning Data...")

# Filling missing Age with median
df["Age"].fillna(df["Age"].median(), inplace=True)

# Filling missing Embarked with mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)


# Droping Cabin column
df.drop("Cabin", axis=1, inplace=True)



print("\nMissing Values After Cleaning:")
print(df.isnull().sum())




# -----------------------------
# 4. How many survived and how many died - Count Plot 
# -----------------------------
plt.figure()
sns.countplot(x="Survived", data=df)
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.show()



# -----------------------------
# 5. Gender vs Survival , survival on bases of gender
# -----------------------------
plt.figure()
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival Based on Gender")
plt.show()



# -----------------------------
# 6. Passenger Class vs Survival , survival on of passenger class
# -----------------------------
plt.figure()
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival Based on Passenger Class")
plt.show()



# -----------------------------
# 7. Age Distribution, kon kon se age ke pasangers the titanic me
# -----------------------------
plt.figure()
sns.histplot(df["Age"], bins=15, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()


 
print("\nThank You for using titanic titanic analysis\n")