products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]

total_discounted_price = sum(
    price * 0.8
    for name, category, price in products
    if category == "Electronics"
)

print(total_discounted_price)
