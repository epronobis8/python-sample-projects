expenses = [10.50, 8, 5, 15, 20, 5, 3]
sum = 0

for x in expenses:
    sum = sum + x

# dont have to convert sum to a string; like in previous examples check roll-dice
# the sep is formatting
print("You spent $", sum, " on lunch this week.", sep='')