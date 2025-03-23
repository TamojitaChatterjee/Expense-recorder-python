# Expense Tracker

This is a simple expense tracker application written in Python that allows you to record your daily expenses, categorize them, view a summary of your spending, generate visual reports, and export the data to an Excel file.

## Features

- Track expenses with amount, description, and category.
- Add new expense categories as needed.
- View total expenses and a breakdown by category.
- Generate a pie chart visualization of expense distribution (matplotlib).
- Export expense data to an Excel file (pandas & openpyxl).

## Versions
This repository contains three different versions of the Expense Tracker:

### 1. **CLI-Based Expense Tracker (`exp_tracker_reg.py`)**
- Basic command-line interface (CLI) for adding and viewing expenses.
- Displays a text-based summary of total and categorized expenses.
- Does **not** include graphical charts or Excel export.

### 2. **Expense Tracker with Pie Chart (`exp_tracker_pie.py`)**
- Extends the basic tracker with **pie chart visualization** using `matplotlib`.
- Generates a graphical representation of expense distribution by category.
- Provides an additional menu option to display the pie chart.

### 3. **Expense Tracker with Excel Export (`exp_tracker_excel.py`)**
- Includes **Excel export functionality** using `pandas` and `openpyxl`.
- Saves the expenses to an `expenses.xlsx` file for future reference.
- Retains the **pie chart feature** from the second version.

## Installation
To run the Expense Tracker, ensure you have Python installed along with the necessary dependencies:

```sh
pip install matplotlib pandas openpyxl
```

## Running the Scripts
Navigate to the directory where the files are located and run the desired script:

For the basic CLI version:
```sh
python exp_tracker_reg.py
```
For the version with a pie chart:
```sh
python exp_tracker_pie.py
```
For the version with Excel export:
```sh
python exp_tracker_excel.py
```

## How to Use
The program presents a menu-driven interface. Here's what each option does:

1. **Add Expense**
   - Enter the amount, description, and category.
   - You can also create a new category if it's not already listed.
2. **View Summary**
   - Displays the total amount spent and a breakdown of expenses by category.
3. **Generate Pie Chart (Available in `exp_tracker_pie.py` and `exp_tracker_excel.py`)**
   - Displays a pie chart representing expense distribution.
4. **Export to Excel (Available in `exp_tracker_excel.py`)**
   - Saves expenses in `expenses.xlsx` for record-keeping.
5. **Exit**
   - Terminates the program.

## Example Usage
1. Choose option `1` to add an expense.
2. Enter the amount (e.g., `25.50`).
3. Enter a description (e.g., `Groceries`).
4. Select a category from the list or enter a new one (e.g., `Shopping`).
5. The program confirms the expense is added.
6. Choose option `2` to view the summary.
7. Optionally, use `3` (Pie Chart) or `4` (Excel Export) in applicable versions.
