import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# CONFIGURATION
NUM_CUSTOMERS = 5000
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2026, 1, 1)

def generate_saas_data():
    data = []
    
    for i in range(NUM_CUSTOMERS):
        customer_id = f"CUST-{1000+i}"
        
        # 1. Acquisition Details
        # Random join date between 2023 and 2026
        days_range = (END_DATE - START_DATE).days
        join_date = START_DATE + timedelta(days=random.randint(0, days_range))
        
        # 2. Subscription Details
        plan_type = np.random.choice(['Startup (Monthly)', 'Enterprise (Annual)'], p=[0.7, 0.3])
        mrr = 5000 if plan_type == 'Startup (Monthly)' else 25000 # Monthly Recurring Revenue
        
        # 3. Behavior Metrics (The "Why")
        # High support tickets = Frustrated customer
        support_tickets = np.random.poisson(2) 
        # Low usage = Disengaged customer
        feature_usage_score = np.random.normal(60, 20) # 0 to 100 scale
        feature_usage_score = max(0, min(100, feature_usage_score))
        
        # 4. Churn Logic (The "Target")
        # Probability of churn increases if: Monthly Plan, High Tickets, Low Usage
        prob_churn = 0.02 # Base monthly churn
        
        if plan_type == 'Startup (Monthly)': prob_churn += 0.05
        if support_tickets > 4: prob_churn += 0.15
        if feature_usage_score < 30: prob_churn += 0.20
        
        # Determine if they churned
        # We simulate tenure based on geometric distribution of churn probability
        tenure_months = np.random.geometric(prob_churn)
        
        # Calculate Churn Date
        churn_date = join_date + timedelta(days=tenure_months*30)
        
        # Censoring: If churn date is in the future (after today), they are still active
        if churn_date > END_DATE:
            is_churned = 0
            churn_date = None
            tenure_months = (END_DATE - join_date).days // 30
        else:
            is_churned = 1
            
        # Ensure tenure is at least 1 month
        tenure_months = max(1, tenure_months)
        
        data.append({
            'Customer_ID': customer_id,
            'Join_Date': join_date,
            'Plan_Type': plan_type,
            'MRR': mrr,
            'Support_Tickets_Per_Month': support_tickets,
            'Feature_Usage_Score': round(feature_usage_score, 1),
            'Tenure_Months': tenure_months,
            'Churned': is_churned
        })

    return pd.DataFrame(data)

# GENERATE & SAVE
df = generate_saas_data()
print(f"Generated {len(df)} B2B SaaS customers.")
print(f"Overall Churn Rate: {df['Churned'].mean()*100:.1f}%")
df.to_csv('saas_customer_data.csv', index=False)