menu = ['spam1', 'spam2', 'spam3', 'spam4']
menu_prices = {}
price = 0.50

for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)