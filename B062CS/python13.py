def normalize_and_filter(words):
        result = []
        for word in words:
            normalized = word.strip().lower()
            if len(normalized) > 5:
                result.append(normalized)
        return result
# Example usage
words = ["Pyhton", "ai", "machine", "data"]
output = normalize_and_filter(words)
print(output)  # Output: ['python', 'machine']

########################################################
def calculate_total_revenue(customers):
    total_revenue = 0.0
    for customer in customers:
            for purchase in customer["purchases"]:
                if purchase >= 100:
                    total_revenue += purchase * 1.1
    return total_revenue

# Example usage
customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]
output = calculate_total_revenue(customers)
print(output)  # Output: 990.0

#################################################################
def calculate_total_discounted_price(products):
    total = 0.0
    for product in products:
        name, category, price = product
        if category == "Electronics":
            discounted_price = price * 0.8
            total += discounted_price
    return total

# Example usage
products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
output = calculate_total_discounted_price(products)
print(output)  # Output: 1200.0

############################################################

def calculate_total_updated_marks(students):
    total_marks = 0
    for student in students:
        marks = student["marks"]
        average = sum(marks) / len(marks)
        if average >= 60:
            for mark in marks:
                updated_mark = mark + 5
                total_marks += updated_mark
    return total_marks

# Example usage
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]
output = calculate_total_updated_marks(students)
print(output)  # Output: 375

######################################################
def calculate_grand_total(regions):
    grand_total = 0.0
    for region in regions:
        region_total = 0.0
        for store in region["stores"]:
            for transaction in store["transactions"]:
                if transaction["successful"] and transaction["category"] == "Electronics" and transaction["amount"] >= 100:
                    taxed_amount = transaction["amount"] * 1.18 * 1.05
                    region_total += taxed_amount
        grand_total += region_total
    return grand_total

# Example usage
regions = [
    {
        "region": "North",
        "stores": [
            {
                "transactions": [
                    {"amount": 200, "category": "Electronics", "successful": True},
                    {"amount": 50, "category": "Electronics", "successful": True},
                    {"amount": 500, "category": "Clothing", "successful": True}
                ]
            }
        ]
    },
    {
        "region": "South",
        "stores": [
            {
                "transactions": [
                    {"amount": 300, "category": "Electronics", "successful": True},
                    {"amount": 150, "category": "Electronics", "successful": False}
                ]
            }
        ]
    }
]
output = calculate_grand_total(regions)
print(output)  # Output: 619.5


