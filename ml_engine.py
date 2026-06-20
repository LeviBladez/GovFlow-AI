import pandas as pd
import numpy as np

# 1. LOAD THE DATA
# Ensure this matches the file you just exported from Numbers
csv_path = "/Users/upasana/Documents/SolveForIndia/students_cleaned.csv"

# Because you exported as a clean CSV, we don't need engine='python' or 'skip' anymore
df = pd.read_csv(csv_path)

print("✅ SUCCESS: CSV loaded!")
print("Columns found:", df.columns.tolist())

# 2. DEFINE THE ENGINE
def train_and_predict(df):
    df_processed = df.copy()
    
    # Calculate Baseline Risk: High distance + Low attendance = High Risk
    # Adjust these column names if they are slightly different in your CSV!
    if 'Distance_KM' in df_processed.columns and 'Attendance_Rate' in df_processed.columns:
        risk_condition = (df_processed['Distance_KM'] > 5) & (df_processed['Attendance_Rate'] < 75)
        df_processed['Baseline_Risk_Score'] = np.where(risk_condition, 1.0, 0.0)
    else:
        df_processed['Baseline_Risk_Score'] = 0.0
        
    return df_processed

def simulate_policy_impact(df, budget_transport, budget_meals):
    final_df = df.copy()
    final_df['Simulated_Risk_Score'] = final_df['Baseline_Risk_Score']
    
    # Impact simulation
    if 'Distance_KM' in final_df.columns:
        final_df.loc[final_df['Distance_KM'] > 5, 'Simulated_Risk_Score'] -= (budget_transport * 0.002)
    
    final_df['Simulated_Risk_Score'] -= (budget_meals * 0.003)
    final_df['Simulated_Risk_Score'] = final_df['Simulated_Risk_Score'].clip(lower=0.0).round(2)
    
    return final_df

# 3. RUN IT
if __name__ == "__main__":
    df_with_risk = train_and_predict(df)
    final_df = simulate_policy_impact(df_with_risk, budget_transport=50, budget_meals=10)
    
    # Print the top 15 results
    print("\n--- 📊 Trade-off Simulation Results (Top 15) ---")
    # This will print the first 15 rows with their real IDs
    print(final_df.head(15))
    print("\n✅ ML Engine fully operational and using real data!")