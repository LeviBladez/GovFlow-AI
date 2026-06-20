# 🏛️ GovFlow-AI: Policy Simulation & Trade-off Engine

**Transforming noisy, delayed public education data into actionable governance insights.**

GovFlow-AI is a predictive Machine Learning dashboard built for government officials and policymakers. Instead of allocating millions in budgets using static, outdated spreadsheets, GovFlow-AI allows decision-makers to simulate the real-time impact of their spending on high-risk populations.

## ⚠️ The Problem
Public policy is often a guessing game. When officials increase a budget for "Transport Subsidies" or "Mid-Day Meals," they cannot immediately see how that money impacts the dropout risk of individual students. This leads to wasted resources and blind governance.

## 💡 The Solution
We built an interactive, plug-and-play ML engine that calculates a "Baseline Risk Score" for students based on real-world metrics (like Distance from school and Attendance Rate). Through our interactive dashboard, policymakers can adjust budget sliders and watch the AI engine instantly recalculate the projected drop in high-risk students—proving ROI *before* a single rupee is spent.

---

## ✨ Key Features
* **Live Budget Simulation:** Interactive sliders for Transport Subsidies and Mid-Day Meal expansions that feed directly into a live Python ML engine.
* **Instant Trade-off Analysis:** Dynamic visual metrics that calculate exactly how many students are "saved" (moved below the high-risk threshold) by specific funding allocations.
* **🛑 Human-in-the-Loop (HITL) Architecture:** We believe AI should not make blind decisions about human lives. Our built-in override system allows local experts to interrupt the AI, correct a student's risk status based on offline context, and mandate an Audit Log for transparency.

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Reactive UI, dynamic metrics)
* **Backend Engine:** Python (`ml_engine.py`)
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Logistic Regression / Random Forest architecture)

---

## 🚀 How to Run Locally

Follow these steps to run GovFlow-AI on your own machine.

**1. Clone the repository**
```
git clone <https://github.com/LeviBladez/GovFlow-AI>
cd GovFlow-AI
```

**2. Create a Virtual Environment**
Keep your dependencies isolated by creating a virtual environment:
 * **Mac/Linux:** ```python3 -m venv .venv```
 * **Windows:** ```python -m venv .venv```
**3. Activate the Environment**
 * **Mac/Linux:** ```source .venv/bin/activate```
 * **Windows:** ```.venv\Scripts\activate```
**4. Install Dependencies**
```
pip install -r requirements.txt
```

**5. Launch the Dashboard**
```
streamlit run app.py
```
*The app will automatically open in your default web browser at http://localhost:8501.*
## 📂 Project Structure
 * app.py: The main Streamlit application and UI director.
 * ml_engine.py: The backend mathematical brain handling baseline calculations and policy simulation logic.
 * students_cleaned.csv: The primary dataset containing sanitized, anonymized student metrics.
 * requirements.txt: The exact Python environment dependencies required to run the project.
## 🌍 Scalability & Future Vision
While this Minimum Viable Product (MVP) focuses on public education and student dropout rates, the GovFlow-AI architecture is fully modular. The underlying engine can be scaled to support:
 * **Healthcare:** Simulating the impact of regional clinic funding on preventative care rates.
 * **Infrastructure:** Projecting the economic ROI of targeted road repairs.
 * **Defense Logistics:** Optimizing supply chain allocations for remotely operated vehicles.
```
