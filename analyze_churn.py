import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter

# 1. LOAD DATA
df = pd.read_csv('saas_customer_data.csv')
df['Join_Date'] = pd.to_datetime(df['Join_Date'])

# 2. COHORT ANALYSIS (The "Retention Heatmap")
# Group by Join Month (Cohort) and Tenure
df['Cohort_Month'] = df['Join_Date'].dt.to_period('M')

# We calculate retention simply by looking at tenure distribution for visualization
# For a true cohort table, we'd need month-by-month logs, but we can approximate risk zones here.

print("--- SAAS HEALTH METRICS ---")
avg_churn_tenure = df[df['Churned']==1]['Tenure_Months'].median()
print(f"Median Lifetime of Churned Customers: {avg_churn_tenure:.1f} Months")
print(f"Annual Enterprise Churn Rate: {df[df['Plan_Type']=='Enterprise (Annual)']['Churned'].mean()*100:.1f}%")
print(f"Monthly Startup Churn Rate: {df[df['Plan_Type']=='Startup (Monthly)']['Churned'].mean()*100:.1f}%")

# 3. SURVIVAL ANALYSIS (Kaplan-Meier Curve)
kmf = KaplanMeierFitter()

plt.figure(figsize=(10, 6))

# Segment 1: Monthly Plan
monthly_cust = df[df['Plan_Type'] == 'Startup (Monthly)']
kmf.fit(monthly_cust['Tenure_Months'], event_observed=monthly_cust['Churned'], label='Startup (Monthly)')
kmf.plot_survival_function(ci_show=False)

# Segment 2: Annual Plan
annual_cust = df[df['Plan_Type'] == 'Enterprise (Annual)']
kmf.fit(annual_cust['Tenure_Months'], event_observed=annual_cust['Churned'], label='Enterprise (Annual)')
kmf.plot_survival_function(ci_show=False)

plt.title('Customer Survival Curve: When do they cancel?')
plt.xlabel('Tenure (Months)')
plt.ylabel('Survival Probability (Retention Rate)')
plt.grid(True, alpha=0.3)
plt.axvline(x=3, color='red', linestyle='--', label='The "3-Month Cliff"')
plt.legend()
plt.show()

# 4. CHURN DRIVERS (Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(x='Churned', y='Feature_Usage_Score', data=df)
plt.title('Feature Usage Score vs. Churn')
plt.xlabel('Customer Status (0=Active, 1=Churned)')
plt.ylabel('Usage Score (0-100)')
plt.show()