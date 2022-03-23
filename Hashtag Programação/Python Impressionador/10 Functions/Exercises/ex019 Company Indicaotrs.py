"""
# 1
- Some companies consider that the client is in default when he owes more than X R$
- Some companies consider that the seller reached the goal when he sold more than X R$, other consider the seller, the store's sales, stock, time, etc.
- Some companies define that a product is low in stock when it is under X unities....
And others several indicators
"""


# Create a function that calculates the company's inventory' (Stockout)
# Stockout → (lost sales by inventories) / (successfully sales + lost sales by inventories)
# Your program receive a dict with all company sales, the status (Completed or Canceled), if had been canceled the reason for cancellation.

sales = {
    "SL0001": (10000, "Completed", "Little Stock"),
    "SL0002": (11000, "Canceled", "Canceled by costumer"),
    "SL0003": (12000, "Completed", ""),
    "SL0004": (13000, "Completed", ""),
    "SL0005": (14000, "Canceled", "Canceled by costumer"),
    "SL0006": (15000, "Completed", ""),
    "SL0007": (16000, "Completed", "Little Stock"),
    "SL0008": (17000, "Canceled", "Little Stock"),
    "SL0009": (18000, "Completed", ""),
    "SL0010": (19000, "Completed", ""),
    "SL0011": (20000, "Canceled", "Canceled by costumer"),
    "SL0012": (21000, "Completed", "Little Stock"),
    "SL0013": (22000, "Completed", ""),
    "SL0014": (23000, "Canceled", "Little Stock"),
    "SL0015": (24000, "Completed", ""),
}

def stockout_calculation(dict_sales):
    numerator = denominator = 0
    for sale in dict_sales.values():
        values, status, reason = sale
        if status == "Completed":
            denominator += values
        elif status == "Canceled" and reason == "Little Stock":
            denominator += values
            numerator += values
    return numerator / denominator


result = stockout_calculation(sales)
print(result) # Stockout


# 2
# Whe are the default costumers? Find and sed this list to the corresponding sector
# Your function should receive a list of clients and analyze using the CPF
# (CPF, debt, how_many_days)   condition (debt == 1000 days == More than 20)

debtor_customers = [
    ("198.193.000-02", 861, 24),
    ("002.644.870-01", 5213, 19),
    ("135.088.790-03", 2000, 15),
    ("025.107.830-25", 4561, 41),
    ("010.735.040-85", 1500, 8),
    ("197.481.430-07", 1267, 22),
    ("010.101.480-52", 412, 34),
    ("868.215.530-33", 984, 78),
    ("635.267.690-10", 7400, 16),
    ("561.289.620-41", 1489, 49),
]


def default_customers(debtor):
    send_to_finance_sector = []
    for client in debtor:
        CPF, debt, days = client # Unpacking
        if debt >= 1000 and days >= 20:
            send_to_finance_sector.append(CPF)
    return send_to_finance_sector


result = default_customers(debtor_customers)
print(result)
