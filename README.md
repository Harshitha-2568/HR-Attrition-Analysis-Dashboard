# HR-Attrition-Analysis-Dashboard

End-to-end HR Attrition analysis with Python, PowerBI, MySQL and ML to predict employee churn.

## Project Overview
This project analyzes employee attrition data to understand why employees leave a company. 
The goal is to find key patterns and build a dashboard + ML model to predict who is likely to leave.

## Key Objectives
- Analyze HR data to find attrition trends
- Identify main factors causing employees to leave
- Build an interactive PowerBI dashboard for HR insights
- Develop a Machine Learning model to predict employee churn

## Tech Stack
- **Language**: Python
- **Database**: MySQL
- **Visualization**: PowerBI / Streamlit
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **IDE**: VS Code / Jupyter Notebook

## Files in this Repo
- `analysis.py` - Data cleaning and EDA
- `dashboard.py` - Streamlit dashboard code
- `hr_attrition_dashboard.py` - Main app file
- `HR_Attrition_Dashboard_Harshitha.png

## Key Insights
1. Attrition is higher in certain age groups and departments
2. Salary, work-life balance, and job satisfaction are major factors
3. ML model achieved ~85% accuracy in predicting churn

## How to Run
1. Clone this repository
2. Install requirements: `pip install pandas numpy matplotlib seaborn scikit-learn streamlit mysql-connector-python`
3. Setup MySQL database and import dataset
4. Run Streamlit app: `streamlit run dashboard.py`



