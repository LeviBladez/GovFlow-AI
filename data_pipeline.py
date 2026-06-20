import pandas as pd
import numpy as np

def generate_messy_data(num_students=5000):
    print("Fetching and generating raw public data...")
    np.random.seed(42) # For reproducibility during the hackathon
    
    # Generate baseline data
    data = {
        'Student_ID': range(1001, 1001 + num_students),
        'Distance_KM': np.random.uniform(1.0, 20.0, num_students),
        'Family_Income': np.random.choice(['Low', 'Medium', 'High'], num_students, p=[0.5, 0.3, 0.2]),
        'Gender': np.random.choice(['Male', 'Female'], num_students),
        # TARGET VARIABLE: Did they drop out?
        'Dropped_Out': np.random.choice([0, 1], num_students, p=[0.82, 0.18]) 
    }
    
    df = pd.DataFrame(data)
    
    # INJECT NOISE: Simulate missing government attendance logs (15% missing)
    attendance = np.random.normal(75, 15, num_students)
    attendance = np.clip(attendance, 30, 100) # Keep between 30% and 100%
    mask = np.random.rand(num_students) < 0.15
    attendance[mask] = np.nan 
    df['Attendance_Rate'] = attendance

    return df

def clean_data(df):
    print("Running automated imputation for delayed datasets...")
    
    # Clean 1: Impute missing attendance with the median
    median_attendance = df['Attendance_Rate'].median()
    df['Attendance_Rate'].fillna(median_attendance, inplace=True)
    
    # Clean 2: One-Hot Encode categorical variables so the ML models can read them
    df = pd.get_dummies(df, columns=['Family_Income', 'Gender'], drop_first=True)
    
    return df

if __name__ == "__main__":
    # Execute the pipeline
    raw_df = generate_messy_data()
    clean_df = clean_data(raw_df)
    
    # Save the cleaned data to a CSV for the ML Engine to use
    clean_df.to_csv("students_cleaned.csv", index=False)
    print("Pipeline complete. Saved 'students_cleaned.csv'.")
