expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        expenses.append((category, amount))
        print("Expense added!")

    elif choice == "2":
        for expense in expenses:
            print(expense)

    elif choice == "3":
        total = sum(amount for category, amount in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
