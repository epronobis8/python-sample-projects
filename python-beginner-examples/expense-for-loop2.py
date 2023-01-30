total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
#going to loop and ask the user for 7 expenses.
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("Your total is $", total, sep='')