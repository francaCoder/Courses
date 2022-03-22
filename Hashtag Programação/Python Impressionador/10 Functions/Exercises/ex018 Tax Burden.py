price = 1500
cost = 400
profit = 800


def calculate_tax_burden(price, cost, profit):
    tax = price - cost - profit
    burden = tax / price
    return burden


print(f"Tax Burden → {calculate_tax_burden(price, cost, profit):.1%}")
