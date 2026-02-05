# 📉 B2B SaaS Customer Analytics & Churn Prediction

![Status](https://img.shields.io/badge/Status-Completed-success)
![Tech](https://img.shields.io/badge/Tech-Python%20%7C%20Lifelines%20%7C%20Seaborn-blue)
![Domain](https://img.shields.io/badge/Domain-Product%20Analytics-orange)

## 📌 Project Overview
For B2B SaaS companies, "Churn" is the silent killer of growth. This project analyzes subscription data to diagnose **when** customers leave (Survival Analysis) and **why** they leave (Behavioral Analytics).

I simulated a dataset reflecting a Bangalore-based CRM company to perform **Cohort Analysis** and calculate the **"Time-to-Event"** metrics using the Kaplan-Meier estimator.

---

## 📸 Key Findings

### 1. The "Retention Cliff" (Survival Analysis)
Using the `lifelines` library, I plotted the survival curve for different subscription types.

<img width="1252" height="837" alt="Screenshot 2026-02-05 172620" src="https://github.com/user-attachments/assets/ff32df82-c6a2-4fb6-a814-e8f79950a900" />
*(Figure 1: The Blue line (Monthly Plan) shows a steep drop in the first 90 days, identifying a critical "Onboarding Risk" period. The Orange line (Annual Plan) demonstrates significantly higher stability.)*

### 2. The "Engagement" Signal
Does product usage predict retention?

<img width="1002" height="712" alt="Screenshot 2026-02-05 172633" src="https://github.com/user-attachments/assets/175db405-21c3-430f-b740-f8f8377fc102" />
*(Figure 2: Churned customers (Right) display a wider distribution of low usage scores, with many dropping to near-zero engagement prior to cancellation.)*

---

## 🧠 Business Recommendations
Based on the survival curves and usage data, I propose the following interventions:

1.  **Fix the "90-Day Cliff":** Implement a "Concierge Onboarding" program specifically for Monthly Plan users to push them past the critical Month 3 mark.
2.  **Usage Alerts:** Trigger an automatic "Success Manager Outreach" if a customer's Feature Usage Score drops below 30 (the danger zone identified in the boxplot).
3.  **Pricing Strategy:** Incentivize the switch from Monthly to Annual plans with a 20% discount, as Annual cohorts have a 2x higher Lifetime Value (LTV).

---

## 🛠️ Tech Stack
* **Python:** Data generation and processing.
* **Lifelines:** Specialized library for Survival Analysis (Kaplan-Meier curves).
* **Seaborn:** Statistical visualization.
* **Pandas:** Cohort manipulation.

## 🚀 How to Run
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/SaaS-Customer-Analytics.git](https://github.com/YOUR_USERNAME/SaaS-Customer-Analytics.git)
    ```
2.  **Install Requirements:**
    ```bash
    pip install pandas matplotlib seaborn lifelines
    ```
3.  **Step 1: Generate Data**
    ```bash
    python generate_saas_data.py
    ```
4.  **Step 2: Run Analysis**
    ```bash
    python analyze_churn.py
    ```
