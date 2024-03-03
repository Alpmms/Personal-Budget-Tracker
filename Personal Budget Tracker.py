#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

class PersonalBudgetTracker:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, amount: float, description: str, date: dt.date):
        self.expenses.append({"amount": amount, "description": description, "date": date})

    def add_income(self, amount: float, description: str, date: dt.date):
        self.incomes.append({"amount": amount, "description": description, "date": date})

    def generate_report(self):
        total_expenses = sum([expense["amount"] for expense in self.expenses])
        total_incomes = sum([income["amount"] for income in self.incomes])
        net_amount = total_incomes - total_expenses

        expenses_df = pd.DataFrame(self.expenses).sort_values(by="date")
        incomes_df = pd.DataFrame(self.incomes).sort_values(by="date")

        expenses_df["type"] = "Expense"
        incomes_df["type"] = "Income"

        all_transactions = pd.concat([expenses_df, incomes_df], ignore_index=True)

        all_transactions["date"] = pd.to_datetime(all_transactions["date"])
        all_transactions.set_index("date", inplace=True)

        return all_transactions, net_amount

    def display_report(self):
        all_transactions, net_amount = self.generate_report()

        print("Net amount: ${:.2f}".format(net_amount))

        all_transactions.groupby("type").sum().plot(kind="bar", rot=0)
        plt.title("Expenses and Incomes")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()

        all_transactions.groupby("type").sum().plot(kind="pie", autopct="%1.1f%%")
        plt.title("Expenses and Incomes")
        plt.show()

if __name__ == "__main__":
    budget = PersonalBudgetTracker()

    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. Add income")
        print("3. Display report")
        print("4. Quit")

        option = int(input("Enter an option: "))

        if option == 1:
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            date = dt.datetime.strptime(input("Enter the date (yyyy-mm-dd): "), "%Y-%m-%d").date()

            budget.add_expense(amount, description, date)

        elif option == 2:
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            date = dt.datetime.strptime(input("Enter the date (yyyy-mm-dd): "), "%Y-%m-%d").date()

            budget.add_income(amount, description, date)

        elif option == 3:
            budget.display_report()

        elif option == 4:
            break

        else:
            print("Invalid option")


# In[ ]:




