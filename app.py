import streamlit as st
import json
from main import load_positions_from_dict, TeamSelector

st.set_page_config(page_title="🧠 BudgetWise Recruiter", layout="centered")
st.title("💼 BudgetWise Recruiter")

st.markdown("Upload a JSON file of candidates and enter your hiring budget to find the best performing team.")

# Upload file
uploaded_file = st.file_uploader("📤 Upload a candidates JSON file", type=["json"])

# Budget input
budget = st.number_input("💰 Enter your salary budget (Rs.)", min_value=10000, value=250000, step=5000)

if st.button("🚀 Find Best Team"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a candidate JSON file.")
    else:
        try:
            # Load JSON data
            data = json.load(uploaded_file)

            # Load positions and run optimizer
            positions = load_positions_from_dict(data)
            selector = TeamSelector(positions, budget)
            best_team, total_salary = selector.select_best_team()

            if best_team:
                st.success(f"✅ Best team found! Total Salary: Rs. {total_salary}")
                st.markdown("### 🧾 Selected Team:")
                result = {
                    "Position": [],
                    "Name": [],
                    "Salary (Rs.)": []
                }
                for pos, candidate in zip(data.keys(), best_team):
                    result["Position"].append(pos)
                    result["Name"].append(candidate.name)
                    result["Salary (Rs.)"].append(candidate.salary)
                st.table(result)
            else:
                st.error("❌ No valid team can be formed under the given budget.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
