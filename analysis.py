import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# 2. See first 5 rows
print("First 5 rows:")
print(df.head())

# 3. How many people left vs stayed
print("\nAttrition Count:")
print(df['Attrition'].value_counts())

# 4. Basic graph: Attrition by Department
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title('Attrition by Department')
plt.show()