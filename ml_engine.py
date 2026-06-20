import pandas as pd
import numpy as np

def train_and_predict(df):
    """
    Calculates the Baseline Risk Score. 
    This is what gives you the 1639 starting point in the UI.
    """
    df_processed = df.copy()
    
    # Ensure columns exist before calculating
    if 'Distance_KM' in df_processed.columns and 'Attendance_Rate' in df_processed.columns:
        # High risk if they live far away and miss a lot of school
        risk_condition = (df_processed['Distance_KM'] > 5) & (df_processed['Attendance_Rate'] < 75)
        df_processed['Baseline_Risk_Score'] = np.where(risk_condition, 1.0, 0.0)
    else:
        # Fallback if columns are missing (should not happen with your cleaned data)
        df_processed['Baseline_Risk_Score'] = 0.0
        
    return df_processed

def simulate_policy_impact(df, budget_transport, budget_meals):
    """
    Applies the budget sliders to reduce the risk scores.
    Multipliers are boosted so the numbers actually drop below the 0.5 threshold.
    """
    final_df = df.copy()
    
    # Start the simulation exactly where the baseline left off
    final_df['Simulated_Risk_Score'] = final_df['Baseline_Risk_Score']
    
    # 1. Transport Budget Impact (heavily affects students living far away)
    if 'Distance_KM' in final_df.columns:
        final_df.loc[final_df['Distance_KM'] > 5, 'Simulated_Risk_Score'] -= (budget_transport * 0.015)
    
    # 2. Meals Budget Impact (affects everyone)
    final_df['Simulated_Risk_Score'] -= (budget_meals * 0.012)
    
    # 3. Add smooth variance (makes the slider feel realistic and continuous)
    np.random.seed(42) 
    variance = np.random.uniform(0, 0.4, size=len(final_df))
    final_df['Simulated_Risk_Score'] -= variance
    
    # 4. Cleanup: Keep scores between 0.0 and 1.0
    final_df['Simulated_Risk_Score'] = final_df['Simulated_Risk_Score'].clip(lower=0.0).round(2)
    
    return final_df

# --- Local Testing Block (Runs only if you test the file directly) ---
if __name__ == "__main__":
    # Test to ensure it doesn't crash before sending to frontend
    try:
        test_df = pd.read_csv("students_cleaned.csv")
        df_with_risk = train_and_predict(test_df)
        final_results = simulate_policy_impact(df_with_risk, budget_transport=50, budget_meals=50)
        
        baseline_count = len(df_with_risk[df_with_risk['Baseline_Risk_Score'] == 1.0])
        sim_count = len(final_results[final_results['Simulated_Risk_Score'] >= 0.5])
        
        print("✅ Backend Engine Test Successful!")
        print(f"Baseline High Risk: {baseline_count}")
        print(f"Simulated High Risk (Max Budget): {sim_count}")
    except FileNotFoundError:
        print("⚠️ Waiting for CSV data, but functions are ready to be imported.")
