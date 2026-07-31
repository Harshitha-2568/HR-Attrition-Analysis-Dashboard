import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")
st.title("📊 HR Attrition Analysis Dashboard")
st.write("Analyzing employee attrition data")

# Load data
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", len(df))
col2.metric("Employees Who Left", df[df['Attrition']=='Yes'].shape[0])
col3.metric("Attrition Rate", f"{(df[df['Attrition']=='Yes'].shape[0]/len(df))*100:.2f}%")

st.divider()

# Chart 1: Attrition by Department
st.subheader("Attrition by Department")
fig1, ax1 = plt.subplots(figsize=(10,4))
sns.countplot(data=df, x='Department', hue='Attrition', ax=ax1)
plt.xticks(rotation=0)
st.pyplot(fig1)

# Chart 2: Attrition by Age
st.subheader("Attrition by Age")
fig2, ax2 = plt.subplots(figsize=(10,4))
sns.histplot(data=df, x='Age', hue='Attrition', multiple='stack', bins=20, ax=ax2)
st.pyplot(fig2)

# Chart 3: Salary vs Attrition
st.subheader("Monthly Income vs Attrition")
fig3, ax3 = plt.subplots(figsize=(10,4))
sns.boxplot(data=df, x='Attrition', y='MonthlyIncome', ax=ax3)
st.pyplot(fig3)