# Xpense Tracker
![Xpense Tracker Logo](./logo.png "Xpense Tracker Logo")


-----------------
## 📖 Project Overview

**Xpense Tracker** is a Python-based financial management system designed to help users effectively track their expenses, set monthly budgets, and monitor spending patterns. It integrates user-friendly features like categorizing expenses, generating reports, and alerting users when their spending exceeds budget limits. With a focus on financial literacy and empowerment, this project supports individuals in making informed decisions about their finances.

 Xpense Tracker helps users stay informed, disciplined, and financially literate. The system aligns with the United Nations Sustainable Development Goals (SDGs) by promoting responsible consumption and production practices.

---
## 🗂 **Table of Contents**

1. [Project Overview](#--project-overview) 
2. [Application of Python Concepts and Libraries](#1--core-python-concepts)
3. [SDG Integration](#sdg-integration-goal-12---responsible-consumption-and-production)
4. [Getting Started](#getting-started)  
5. [Menu Options](#menu-options)  
6. [Sample Outputs](#sample-outputs)  
7. [General Instructions](#general-instructions)  

-----
## 🛠️ Application of Python Concepts and Libraries
The Xpense Tracker application is designed with fundamental Python concepts and libraries to deliver a simple, efficient, and user-friendly experience:

### 1. Core Python Concepts
- **Functions:**
  - Modular functions (`add_expense`, `view_expenses`, `generate_report`) divide the program into manageable components, improving readability.
  - Utility functions like `get_valid_amount` and `get_date_input` ensure user inputs are accurate and correctly formatted.

- **Control Flow:**
  - Conditional statements (`if-else`) process user menu selections and handle various program operations.
  - Loops (`while`) maintain interactivity, allowing the program to run continuously until the user exits.

- **Enumerations:**
  - The `Enum` class standardizes expense categories (ex: Food, Transport) for better data consistency and validation.

### 2. Data Structures
- **Lists:** Store expense entries dynamically, enabling efficient addition, modification, and deletion.
- **Dictionaries:** Organize user information and monthly budgets, offering quick access and updates.
- **DefaultDict:** From the `collections` module,  it simplifies data grouping and calculations, especially for monthly expense summaries.
### 3. Key Libraries
- **`datetime`:** Validates and handles dates for accurate logging and tracking.
- **`json`:**  Ensures data persistence by saving user details and expense records in a structured format for future use.
- **`collections`:** Simplifies advanced data handling with `DefaultDict`, making data grouping and calculations easier.
### 4. Error Handling
- **Input Validation:**
  - Prevents invalid inputs by verifying numeric values, correctly formatted dates, and valid menu options.
- **File Handling:**
  - Detects and manages issues like missing or corrupted files, ensuring the program starts with a fresh dataset if needed.
- **User Feedback:**
  - Provides clear and actionable error messages, helping users correct mistakes and continue without interruptions.

---

## 🌍 SDG Integration: Goal 12 - Responsible Consumption and Production 
Xpense Tracker supports **SDG Goal 12** by promoting responsible financial habits.
The program:
- **Encourages Awareness:** Tracks and categorizes expenses, helping users monitor consumption patterns.
- **Fosters Discipline:** Helps users set budgets, avoid overspending, and align spending with financial goals.
- **Empowers Decisions:** Generates monthly reports that provide insights into spending trends, enabling informed choices.
  
By addressing these aspects, Xpense Tracker aligns with the global goal of encouraging sustainable and mindful consumption practices.

---

## 🚀 Getting Started
## 1. Prerequisite:
- Install **Python 3.6** or above: [Download Python](https://www.python.org/downloads/)
- Install **Visual Studio Code**: [Download VS Code](https://code.visualstudio.com/)
- Ensure the `expenses.json` file is in the working directory (or let the program create it on the first run).

## 2. Clone or Download the Repository:
```bash
git clone https://github.com/your-username/xpense-tracker.git
cd xpense-tracker
```

## 3. Run the program:
Open a terminal or command prompt.
Execute the following command:
```bash
python main.py
```
## 4. Using the Program

Once launched, the program will prompt you to enter your name and guide you through a menu of options.  
Use the corresponding numbers to navigate the menu:

```plaintext
XPENSE TRACKER MENU
1. Add Expense
2. View List of Expenses
3. Delete Expense
4. Generate Monthly Report
5. Modify Monthly Budget
6. Reset Data
7. Exit
```

# 🌟 **Menu Options**

| **Feature**                   | **Description**                                                                      |
|------------------------------ |--------------------------------------------------------------------------------------|
| **Add Expense**               | Log a new expense by selecting a category, entering a description, amount, and date. |
| **View List of Expenses**     | Review all recorded expenses in a neat table format.                                 |
| **Delete Expense**            | Remove an unwanted expense by its index number.                                      |
| **Generate Monthly Report**   | View categorized expense summaries and compare them to monthly budgets.              |
| **Modify Monthly Budget**     | Adjust your budget for any specific month as needed.                                 |
| **Reset Data**                | Clear all stored data to start fresh.                                                |
| **Exit**                      | Save your progress and exit the program safely.                                      |

---
# 📊 **Sample Outputs**
<details>
  <summary>View Examples:</summary>
   
## **Adding Expense Example** 
   **Output:**
  ```plaintext
  --- Adding a New Expense ---
  New Expense Added:
    Description: Lunch
    Amount: ₱120.00
    Date: 11-22-2024
    Category: Food
```

## **View List of Expense Example**  
```plaintext
-------------------------- LIST OF EXPENSES ----------------------------------------
+-----+---------------------------------+------------+------------+-----------------+
| No. | Description                     | Amount     | Date       | Category        |
+-----+---------------------------------+------------+------------+-----------------+
| 1   | coffee                          | ₱50.00     | 11-22-2024 | Food            |
+-----+---------------------------------+------------+------------+-----------------+
| 2   | fare                            | ₱200.00    | 11-22-2024 | Transporation   |
+-----+---------------------------------+------------+------------+-----------------+
```
## **Delete Expense Example** 
```plaintext
Enter the no. of the expense to delete: 1
Deleted expense: Lunch - ₱50.00 on 11-22-2024 [Food]  
-------- Data saved successfully. --------
```
## **Generate Monthly Report Example**
```
===== EXPENSE REPORT BY MONTH =====

 *********** November 2024 **********
Category        Amount Spent    Budget     Remaining Budget     Status
--------------------------------------------------------------------------------
Food            ₱74.00          ₱500.00     ₱226.00              Within Budget
Transport       ₱200.00         ₱500.00     ₱226.00              Within Budget
--------------------------------------------------------------------------------
TOTAL EXPENSES: ₱274.00
REMAINING BUDGET: ₱226.00
```
### **Overspending: Monthly Report Example**
```plaintext
===== EXPENSE REPORT: November 2024 =====
Category         Amount Spent     Budget          Remaining Budget     Status
--------------------------------------------------------------------------------
Food             ₱ 600.00         ₱ 1000.00       ₱ -100.00            Over Budget
Transport        ₱ 500.00         ₱ 1000.00       ₱ -100.00            Over Budget
--------------------------------------------------------------------------------
TOTAL EXPENSES: ₱1100.00  
REMAINING BUDGET: ₱-100.00  
WARNING: Over budget by ₱100.00!
```
## **Modify Monthly Budget Example:**
```plaintext
Modify Monthly Budget:
Enter the year (ex: 2024): 2024
Enter the month number (1-12): 11
Enter the new budget for November 2024: 1000

Budget for November 2024 updated to: ₱1000.00  
-------- Data saved successfully. --------
```
</details>

-------
## 📌 **General Instructions**  
- **Step-by-Step Guide:** Follow the on-screen prompts for each menu option.  
- **Input Validation:** Enter values carefully—any invalid input will prompt you to retry.  
- **Automatic Data Saving:** Your data is saved after every operation.
------
