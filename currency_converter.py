exchange_rates = {
    "USD": { "EUR": 0.85, "CAD": 1.25 },
    "EUR": { "USD": 1.18, "CAD": 1.47 },
    "CAD": { "USD": 0.80, "EUR": 1.47 },
}
currencies = ("USD", "EUR", "CAD")

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print("Invalid amount!")

def get_source_currency():
    while True:
        source_currency = input("Source currency (USD/EUR/CAD): ").upper()
        if source_currency not in currencies:
            print("Invalid currency!")
        else:
            return source_currency

def get_target_currency():
    while True:
        target_currency = input("Target currency (USD/EUR/CAD): ").upper()
        if target_currency not in currencies:
            print("Invalid currency!")
        else:
            return target_currency

def convert_currency():
    source_currency = get_source_currency()
    target_currency = get_target_currency()
    amount = get_amount()

    if source_currency == target_currency:
        converted_amount = amount
    else:
        converted_amount = amount * exchange_rates[source_currency][target_currency]

    print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")

convert_currency()