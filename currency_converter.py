while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid amount!")

curriencies = ("USD", "EUR", "CAD")
while True:
    source_currency = input("Source currency (USD/EUR/CAD): ").upper()
    if source_currency not in curriencies:
        print("Invalid currency!")
    else:
        break

while True:
    target_currency = input("Target currency (USD/EUR/CAD): ").upper()
    if target_currency not in curriencies:
        print("Invalid currency!")
    else:
        break

exchange_rates = {
    "USD": { "EUR": 0.85, "CAD": 1.25 },
    "EUR": { "USD": 1.18, "CAD": 1.47 },
    "CAD": { "USD": 0.80, "EUR": 1.47 },
}

converted_amount = amount * exchange_rates[source_currency][target_currency]

print(f"{amount} {source_currency} is equal to {converted_amount}")