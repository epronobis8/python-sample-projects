total = 0
prices = [2.50, 3.50, 4.50]

for price in prices:
    total = total + price
    print(total)

average = total/len(prices)
print('avg is', average)