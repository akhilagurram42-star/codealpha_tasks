stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total = 0

print("Simple Stock Tracker")
print("Type 'done' to finish")
print("My Stock Portfolio Tracker")

while True:
    name = input("Enter stock name: ").upper()

    if name == "DONE":
        break

    if name in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[name] * qty
    else:
        print("Stock not available!")

print("Total Investment Value:", total)