# Xpense Tracker

   LOGO PART
-----------------
## 📖 Project Overview

**Xpense Tracker** is a Python-based financial management system designed to help users effectively track their expenses, set monthly budgets, and monitor spending patterns. It integrates user-friendly features like categorizing expenses, generating detailed reports, and alerting users when their spending exceeds budget limits. With a focus on financial literacy and empowerment, this project supports individuals in making informed decisions about their finances.

 Xpense Tracker helps users stay informed, disciplined, and financially literate. The system aligns with the United Nations Sustainable Development Goals (SDGs) by promoting responsible consumption and production practices.

---

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
## 1. Prerequisites:
- Install **Python 3.6** or above.
- Install **Visual Studio Code (VS Code)**:
  1. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
  2. Install the **Python extension** in VS Code for better development and debugging support.
- Ensure the `expenses.json` file is in the working directory (or let the program create it on the first run).

### 2. Clone or Download the Repository:
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
# 4 Using the Program

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

### **1. Add Expense**  
Easily log a new expense by:  
- Selecting a category (e.g., Food, Transport, Entertainment).  
- Entering a description of the expense.  
- Providing the expense amount and date.  
### **2. View List of Expenses**  
Review all recorded expenses in a neatly formatted table for quick and easy access to details.
### **3. Delete Expense**  
Remove an unwanted expense by selecting its corresponding index number from the list.
### **4. Generate Monthly Report**  
Get a summarized report of your monthly spending:  
- Categorized breakdowns of expenses.  
- Budget comparisons to identify areas of overspending or savings.  
### **5. Modify Monthly Budget**  
Adjust the budget for any specific month to stay aligned with your evolving financial goals.
### **6. Reset Data**  
Clear all stored data to start fresh.  
*(Note: This action requires confirmation and will delete all expenses and budgets.)*
### **7. Exit**  
Save your progress and exit the program safely.

---

## 📌 **General Instructions**  
- **Step-by-Step Guide:** Follow the on-screen prompts for each menu option.  
- **Input Validation:** Enter values carefully—any invalid input will prompt you to retry.  
- **Automatic Data Saving:** Your data is saved after every operation.
------
