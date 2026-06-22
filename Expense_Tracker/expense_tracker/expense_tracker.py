import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class expense_tracker:

    def __init__(self):
        self.file_name = "expenses.csv"
        try:
            self.df = pd.read_csv(self.file_name)
        except:
            self.df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
            self.df.to_csv(self.file_name, index=False)

    # Adding Expense
    def add_expense(self):
        date = input("Enter Date (YYYY-MM-DD): ")
        amount = float(input("Enter Amount: "))
        category = input("Enter Category: ")
        description = input("Enter Description: ")

        if amount <= 0:
            print("Amount must be positive!")
            return

        new_data = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
        self.df.to_csv(self.file_name, index=False)

        print("Expense Added Successfully!\n")

    # summary
    def get_summary(self):
        if self.df.empty:
            print("No Data Available\n")
            return

        amounts = np.array(self.df["Amount"])

        total = np.sum(amounts)
        average = np.mean(amounts)

        print("\n----- Expense Summary -----")
        print("Total Spending:", total)
        print("Average Spending:", round(average, 2))

        print("\nCategory Wise Spending:")
        print(self.df.groupby("Category")["Amount"].sum())
        print()

    # Filtering Expenses
    def filter_expenses(self):
        category = input("Enter category to filter: ")
        filtered = self.df[self.df["Category"] == category]

        if filtered.empty:
            print("No data found\n")
        else:
            print(filtered, "\n")

    # Monthly Report
    def generate_report(self):
        if self.df.empty:
            print("No Data Available\n")
            return

        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df["Month"] = self.df["Date"].dt.to_period("M")

        monthly = self.df.groupby("Month")["Amount"].sum()

        print("\nMonthly Report:")
        print(monthly, "\n")

    # Visualizations
    def visualize_data(self):
        if self.df.empty:
            print("No Data Available\n")
            return

        # Bar Chart
        plt.figure()
        self.df.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Total Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

        # Line Chart
        plt.figure()
        daily = self.df.groupby("Date")["Amount"].sum()
        daily.plot()
        plt.title("Spending Over Time")
        plt.show()

        # Pie Chart
        plt.figure()
        self.df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct='%1.1f%%')
        plt.ylabel("")
        plt.title("Spending Distribution")
        plt.show()

        # Histogram using Seaborn
        plt.figure()
        sns.histplot(self.df["Amount"], bins=5, kde=True)
        plt.title("Expense Distribution")
        plt.show()


# ================= MENU USING MATCH CASE =================

def main():
    tracker = expense_tracker()

    while True:
        print("===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Filter by Category")
        print("4. Monthly Report")
        print("5. Visualize Data")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                tracker.add_expense()
            case 2:
                tracker.get_summary()
            case 3:
                tracker.filter_expenses()
            case 4:
                tracker.generate_report()
            case 5:
                tracker.visualize_data()
            case 6:
                print("Thank You!")
                break
            case _:
                print("Invalid Choice!\n")


if __name__ == "__main__":
    main()