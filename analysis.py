import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
print("First 5 rows:")
print(df.head())
print("\nAttrition Count:")
print(df['Attrition'].value_counts())
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Department', hue='Attrition')
plt.title('Attrition by Department')
plt.show()
