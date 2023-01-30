total = 0
expenses = []

#going to loop and ask the user for 7 expenses.
for i in range(7):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)

print("Your total is $", total, sep='')