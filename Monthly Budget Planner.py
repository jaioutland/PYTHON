'''
Assignment: Monthly Budget Planner
Name: Jai Outland
github link:
'''
def budget_calculator():
    print("Monthly Budget Planner")
    print()

# Usser inputs their montly income    
    income = float(input("Enter Monthly Net Income: $"))
    
    categories = ("Rent/Mortgage", "Utilities", "Groceries", "Transportation", "Health Care", "Personal Care", "Clothing", "Entertainment", "Savings", "Debt", "Other")
    expenses = {}
    print()
    
    print("\nEnter your expenses in the following categories")
    
# User inputs expenses for each category
    Rent_mortgage = float(input("Enter your monthly rent/mortgage: $"))
    Utilities = float(input("Enter your monthly utilities cost: $"))
    Groceries = float(input("Enter your monthly grocery spend: $ "))
    Transportation = float(input("Enter your monthly transportation cost: $"))
    Health_Care = float(input("Enter your montly health care cost: $"))
    Personal_Care = float(input("Enter your monthly personal care cost: $"))
    Clothing = float(input("Enter your monthly clothing costs: $"))
    Entertainment = float(input("Enter your montly entertainment cost: $"))
    Savings = float(input("Enter your monthly Savings: $"))
    Debt = float(input("Enter your debt: $"))
    Other = float(input("Enter other expenses: $"))
    print()
    
# Store all expenses in proper categories
    expenses = {
        "Rent/mortgage": Rent_mortgage,
        "Utilities": Utilities,
        "Groceries": Groceries,
        "Transportation": Transportation,
        "Health Care": Health_Care,
        "Personal Care": Personal_Care,
        "Clothing": Clothing,
        "Entertainment": Entertainment,
        "Savings": Savings,
        "Debt": Debt,
        "Other": Other
    }
    
# Calculate total expenses
    total_expenses = sum (expenses.values())
    print(f"Total Expenses: ${total_expenses:.2f}")
    print()
    
# Calculate remaining balance
    balance = income - total_expenses
    print(f"Remaining Balance: ${balance:.2f}\n")
    
# Display category breakdown
    print("Budget Breakdown")
    for category, amount in expenses.items():
     print(f"{category}: ${amount:.2f}")
     print()
    
    print("\nBudget Analysis Complete ✅")
# Run Function
budget_calculator()