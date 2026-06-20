import streamlit as st
import pandas as pd
from ml_engine import train_and_predict, simulate_policy_impact

# --- PAGE CONFIG ---
st.set_page_config(page_title="GovFlow-AI Dashboard", layout="wide")

st.title("🏛️ GovFlow-AI: Policy Simulation & Trade-off Engine")
st.markdown("Transforming noisy, delayed public education data into actionable governance insights.")
st.divider()

# --- SIDEBAR CONTROLS ---
st.sidebar.header("⚙️ Plug-and-Play AI Engine")
selected_model = st.sidebar.selectbox("Active Prediction Model", ["Logistic Regression", "Random Forest"])

st.sidebar.header("💰 Budget Allocation Simulation")
budget_transport = st.sidebar.slider("Transport Subsidy (Crores)", 0, 50, 10)
budget_meals = st.sidebar.slider("Mid-Day Meal Expansion (Crores)", 0, 50, 15)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    try:
        return pd.read_csv("students_cleaned.csv")
    except FileNotFoundError:
        st.error("Data missing. Please ensure students_cleaned.csv is in the folder.")
        return pd.DataFrame()

df = load_data()

# --- RUN ENGINE & MATH ---
if not df.empty:
    # 1. Baseline
    df_with_risk = train_and_predict(df)
    baseline_high_risk_count = len(df_with_risk[df_with_risk['Baseline_Risk_Score'] == 1.0])

    # 2. Simulation (using slider values)
    final_df = simulate_policy_impact(df_with_risk, budget_transport=budget_transport, budget_meals=budget_meals)
    simulated_high_risk_count = len(final_df[final_df['Simulated_Risk_Score'] >= 0.5])
    
    # 3. Calculate difference for the UI arrow
    students_saved = simulated_high_risk_count - baseline_high_risk_count
else:
    baseline_high_risk_count = 0
    simulated_high_risk_count = 0
    students_saved = 0

# --- MAIN DASHBOARD METRICS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Current Regional Baseline")
    st.markdown("Data based on historical records.")
    st.metric(label="Baseline High-Risk Students", value=baseline_high_risk_count)
    
with col2:
    st.subheader("Simulated Policy Impact")
    st.markdown(f"Using *{selected_model}* | Transport: ₹{budget_transport}Cr | Meals: ₹{budget_meals}Cr")
    st.metric(
        label="Projected High-Risk Students", 
        value=simulated_high_risk_count, 
        delta=f"{students_saved} students",
        delta_color="inverse" # Turns negative numbers green!
    )

st.divider()

# --- HUMAN IN THE LOOP ---
st.header("🛑 Human-in-the-Loop Override")
st.markdown("Interrupt the AI and force a recalculation based on offline knowledge.")

col_override1, col_override2 = st.columns(2)

with col_override1:
    override_id = st.number_input("Target Student/District ID", min_value=1001, max_value=6000, step=1)
    override_action = st.selectbox("Force Risk Level", ["Mark as Safe", "Mark as High Risk"])

with col_override2:
    override_reason = st.text_input("Reason for Intervention (Audit Log)")
    if st.button("Execute Override"):
        if override_reason:
            st.success(f"Audit Logged: Override applied for ID {override_id}. Reason: {override_reason}")
        else:
            st.warning("Please provide a reason to maintain governance transparency.")
