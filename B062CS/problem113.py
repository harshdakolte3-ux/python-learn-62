



"""

#1. Total Revenue from Active Customers
        Problem Statement
        You are given a list of customer dictionaries.
        Each customer has:
        • name
        • purchases → list of purchase amounts
        • active → boolean
        Calculate the total revenue generated only by active customers, but:
        • Ignore purchase amounts less than 100
        • Apply a 10% tax to each valid purchase before summing

        customers = [
            {"name": "A", "purchases": [50, 200, 300], "active": True},
            {"name": "B", "purchases": [500, 20], "active": False},
            {"name": "C", "purchases": [150, 250], "active": True}
        ]
        Output
        990.0

        2. Problem Statement
        You are given a list of products as tuples:

        Task:
        • Keep only products in category "Electronics"
        • Apply a 20% discount
        • Return the total discounted price
        Input
        products = [
            ("Laptop", "Electronics", 1000),
            ("Shirt", "Clothing", 50),
            ("Phone", "Electronics", 500)
        ]
        Output:
        1200.0

        3. Student Weighted Score Calculator
        Problem Statement
        You are given a list of students:

        Task:
        • Keep students whose average is ≥ 60
        • Increase each mark by 5 grace marks
        • Compute the total of all updated marks
        Input
        students = [
            {"name": "A", "marks": [50, 60, 70]},
            {"name": "B", "marks": [30, 40]},
            {"name": "C", "marks": [80, 90]}
        ]

        Output: 
        375








Multi-Region Sales Analytics Engine
Problem Statement
You are given a list of regions. Each region contains multiple stores, and each store contains multiple transactions.
Each transaction has:
• amount (float)
• category (string)
• successful (boolean)
Task
• Consider only transactions that:
• Are successful
• Belong to category "Electronics"
• Have amount ≥ 100
Apply:
• 18% GST to each valid transaction
• Then apply an additional 5% regional surcharge
Compute:
• The total revenue per region
• Then return the grand total across all regions

Input: 
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

#Final output: single float (grand total)
"""