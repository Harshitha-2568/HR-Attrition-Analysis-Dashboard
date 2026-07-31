# hr_attrition_dashboard.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# 2. Chart 1: Overall
plt.figure(figsize=(6,6))
df['Attrition'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen','lightcoral'])
plt.title('Overall Attrition')
plt.ylabel('')
plt.show()

# 3. Chart 2: By Department
attrition_dept = df.groupby('Department')['Attrition'].apply(lambda x: (x=='Yes').mean()*100).sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=attrition_dept.index, y=attrition_dept.values)
plt.title('Attrition Rate by Department %')
plt.xticks(rotation=45)
plt.show()

# 4. Chart 3: By Age
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Age', hue='Attrition')
plt.title('Attrition by Age')
plt.show()

# 5. Chart 4: By Overtime
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='OverTime', y=(df['Attrition']=='Yes').astype(int)*100)
plt.title('Attrition % by Overtime')
plt.ylabel('Attrition %')
plt.show()

# 6. Chart 5: The "one more" Heatmap
pivot = df.pivot_table(index='JobRole', columns='OverTime', values='Attrition', aggfunc=lambda x: (x=='Yes').mean()*100)
plt.figure(figsize=(12,6))
sns.heatmap(pivot, annot=True, fmt='.1f', cmap='Reds')
plt.title('Attrition % by JobRole and Overtime')
plt.show()