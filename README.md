# 💼 BudgetWiseRecruiter

**BudgetWiseRecruiter** is a smart hiring optimization tool built with Python and Streamlit. It helps select the best-performing team within a fixed salary budget by analyzing multiple candidates across different roles — all using an intuitive web interface.

---

## 🚀 Features

✅ Accepts any number of job positions and candidates  
✅ Users upload their own `.json` file (no hardcoded data)  
✅ Calculates the **best team** under a specified budget  
✅ Uses performance-based selection (higher salary = better performer)  
✅ Web-based interface powered by **Streamlit**  
✅ Modular, reusable **object-oriented design (OOP)**

---

## 🧠 How It Works

1. Upload a `.json` file containing candidate data
2. Enter your budget
3. The system finds the **best team** by:
   - Selecting one candidate per position
   - Maximizing total performance (higher salaries)
   - Ensuring total salary stays within budget
4. Results are displayed in a clean table

---

## 📂 Folder Structure
BudgetWiseRecruiter/
├── app.py # Streamlit GUI app
├── main.py # OOP logic for selection
├── requirements.txt # Dependencies
├── README.md # Project overview
└── test_cases/
├── case_1.json 
├── case_2.json 
└── case_3.json

---

## 📤 JSON Input Format

```json
{
  "Supervisor": [["Velma", 50000], ["Daphne", 20000]],
  "Waiter": [["Tom", 40000], ["Jerry", 30000]],
  "Cashier": [["Batman", 100000]],
  "Chef": [["Garfield", 80000], ["Simpson", 150000]],
  "Cleaner": [["Dobby", 30000], ["Scrubby", 60000]]
}
