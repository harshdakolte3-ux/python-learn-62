1.
nums = [1, 2, 2, 3, 3, 3]

result = {}
for num in nums:
    result[num] = result.get(num, 0) + 1

print(result)

2.
data = {"a": 1, "b": 2}
key = "a"

if key in data:
    print("Found")
else:
    print("Not Found")


3.
data = (("a", 1), ("b", 2))

result = dict(data)
print(result)


4.
text = "data science is fun"

reversed_words = text.split()[::-1]
print(reversed_words)

5.
tuples = [(1, 2), (3, 4), (5, 6)]

sums = [a + b for a, b in tuples]
print(sums)

6.
words = ["python", "ml", "ai"]

length_map = {}
for word in words:
    length_map[word] = len(word)

print(length_map)

7.
text = "programming"

seen = set()
unique_chars = []

for ch in text:
    if ch not in seen:
        seen.add(ch)
        unique_chars.append(ch)

result = tuple(unique_chars)
print(result)

8.
numbers = [1, 2, 3, 4, 5, 6]

evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)


9.
students = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]

result = {}
for name, marks in students:
    avg = sum(marks) / len(marks)
    result[name.lower()] = round(avg, 2)

print(result)

10.
import string

sentence = "Python is great and Python is easy"

# Remove punctuation
translator = str.maketrans('', '', string.punctuation)
cleaned = sentence.translate(translator)

# Convert to lowercase and split into words
words = cleaned.lower().split()

# Count frequency
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

11.
sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]

# Sum total sales per product
totals = {}
for product, qty in sales:
    totals[product] = totals.get(product, 0) + qty

# Find the product with the highest total sales
highest_selling = max(totals, key=totals.get)

print(highest_selling)


12.
data = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}

# Use a set to get unique values
unique_values = set()
for values in data.values():
    unique_values.update(values)

# Convert to sorted list
result = sorted(unique_values)
print(result)


13.
attendance = {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}

result = {}
for name, records in attendance.items():
    total_days = len(records)
    present_days = records.count("P")
    percentage = (present_days / total_days) * 100
    result[name] = round(percentage, 2)

print(result)


14.
text = "banana"

char_indices = {}
for idx, ch in enumerate(text):
    if ch in char_indices:
        char_indices[ch] += (idx,)
    else:
        char_indices[ch] = (idx,)

print(char_indices)


15.
dicts = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]

merged = {}
for d in dicts:
    for key, value in d.items():
        merged[key] = merged.get(key, 0) + value

print(merged)
