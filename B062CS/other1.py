## 1
employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]


salaries = list(map(lambda e: e['salary'], employees))


min_sal = min(salaries)
max_sal = max(salaries)


filtered_employees = list(filter(lambda e: e['salary'] != min_sal and e['salary'] != max_sal, employees))

remaining_salaries = list(map(lambda e: e['salary'], filtered_employees))


average = sum(remaining_salaries) / len(remaining_salaries) if remaining_salaries else 0

print(average)  


## 2
emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
allowed_domains = {"gmail.com"}

filtered_emails = list(filter(lambda email: email.split('@')[1] in allowed_domains, emails))

usernames = list(map(lambda email: email.split('@')[0], filtered_emails))

print(usernames)  

##3
students = {
    "Alice": [45, 50, 60],
    "Bob": [35, 55, 65],
    "Charlie": [40, 40, 40]
}

filtered_students = list(filter(lambda item: all(mark >= 40 for mark in item[1]), students.items()))

passed_students = list(map(lambda item: item[0], filtered_students))

print(passed_students)  

## 4
products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
]

converted_products = list(map(lambda p: (p[0], p[1] * 83), products))


filtered_products = list(filter(lambda p: p[1] > 3000, converted_products))

print(filtered_products) 

##5
users = [
    {"name": "A", "user_id": 2, "active": True},
    {"name": "B", "user_id": 4, "active": True},
    {"name": "C", "user_id": 5, "active": False},
    {"name": "D", "user_id": 7, "active": True}
]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

filtered_users = list(filter(lambda u: u['active'] and is_prime(u['user_id']), users))


active_prime_users = list(map(lambda u: u['name'], filtered_users))

print(active_prime_users)  


##6
words = ["  Python ", " AI ", "Machine ", " Data "]

normalized_words = list(map(lambda w: w.strip().lower(), words))

filtered_words = list(filter(lambda w: len(w) >= 5, normalized_words))

print(filtered_words)  