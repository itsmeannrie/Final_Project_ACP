# Xpense Tracker

   LOGO PART
-----------------
## 📖 Project Overview

**Xpense Tracker** is a Python-based financial management application designed to help users effectively track their expenses, set monthly budgets, and monitor spending patterns. It integrates user-friendly features like categorizing expenses, generating detailed reports, and alerting users when their spending exceeds budget limits. With a focus on financial literacy and empowerment, this project supports individuals in making informed decisions about their finances.

This project aligns with the **United Nations Sustainable Development Goal (SDG) 1: No Poverty** by encouraging responsible financial management to reduce personal financial distress and promote sustainable economic growth.

---

## 🛠️ Application of Python Concepts and Libraries

### **1. Core Python Concepts**
- **Control Structures**:
  - Conditional statements (`if-elif-else`) for menu navigation and validations.
  - Loops (`for`, `while`) for iterating over data and retrying user inputs.
- **Data Structures**:
  - Lists for storing multiple expense records.
  - Dictionaries to organize user details and budgets.
  - Default dictionaries (`collections.defaultdict`) for grouping expenses by month and category.

### **2. Python Libraries**
- **`datetime`**:
  - Used to handle date inputs and calculations (e.g., grouping expenses by month).
- **`json`**:
  - Facilitates data persistence by saving and loading user data in a JSON file.
- **`enum`**:
  - Provides predefined expense categories to ensure consistency and easy selection.

### **3. Modular Code Design**
- Functions are modular and reusable, ensuring clarity and maintainability:
  - **Utility Functions** for validating inputs (e.g., numeric values, dates).
  - **Expense Management Functions** for adding, viewing, and deleting expenses.
  - **Budget Management Functions** for setting or modifying monthly budgets.

---

## 🌍 SDG Integration: Goal 1 - No Poverty

### **Alignment with SDG 1**
The project supports **SDG 1: No Poverty**, particularly target **1.4**, which emphasizes access to economic resources. By promoting financial literacy and responsible money management, Xpense Tracker:
- Reduces the likelihood of overspending and financial distress.
- Encourages savings by providing visibility into spending patterns.
- Helps users align their spending with sustainable financial goals.


---

## 🚀 Instructions for Running the Program

### **Prerequisites**
1. Install **Python 3.7** or higher on your system. [Download Python](https://www.python.org/downloads/)
2. Ensure your terminal or command prompt is set up to run Python scripts.

### **Steps to Run**
1. **Clone or Download the Repository**:
   - Clone the project using Git:
     ```bash
     git clone https://github.com/your-repo/xpense-tracker.git
     cd xpense-tracker
     ```
   - Or download the repository as a ZIP file from the GitHub page and extract it to a folder.

2. **Navigate to the Project Directory**:
   ```bash
   cd xpense-tracker
