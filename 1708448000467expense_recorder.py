#expense recorder
#defining list
categories = ["Groceries", "Transportation", "Utilities", "Entertainment"]

expenses = []
#case 1: adding expense
def add_expense():
  amt = float(input("Enter amount: "))
  description = input("Enter description: ")
  category = input("Choose category ({}): ".format(', '.join(categories)))
  if category not in categories:
    categories.append(category)
  expenses.append({"amount": amt, "description": description, "category": category})
  print("Expense added!")
#case 2: displaying summary
def display_summary():
  total_expense = sum(expense["amount"] for expense in expenses)
  print("Total expense:", total_expense)
  category_totals = {}
  for expense in expenses:
    category = expense["category"]
    category_totals[category] = category_totals.get(category, 0) + expense["amount"]
  for category, amount in category_totals.items():
    print(f"{category}: {amount}")
#menu
def main():
  while True:
    print("\nExpense Tracker")
    print("1. Add expense")
    print("2. View summary")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
      add_expense()
    elif choice == "2":
      display_summary()
    elif choice == "3":
      break
    else:
      print("Invalid choice!")

if __name__ == "__main__":
  main()