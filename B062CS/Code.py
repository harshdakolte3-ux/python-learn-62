# 1. Character Count  
s1 = "apple"
char_count = {}
for ch in s1:
    char_count[ch] = char_count.get(ch, 0) + 1
print("1.", char_count)


# 2. Square Number Dictionary
nums = [1, 2, 3, 4]
square_dict = {}
for n in nums:
    square_dict[n] = n * n
print("2.", square_dict)


# 3. Word First Letter Mapping
words1 = ["cat", "dog", "elephant"]
first_letter = {}
for word in words1:
    first_letter[word] = word[0]
print("3.", first_letter)


# 4. Student Score Analyzer
students = [("Amit", [70, 80, 90]), ("Neha", [85, 90, 95])]
avg_marks = {}
for name, marks in students:
    avg_marks[name] = sum(marks) // len(marks)
print("4.", avg_marks)


# 5. Product Sales Aggregator
sales = [("Pen", 10), ("Pencil", 5), ("Pen", 15)]
total_sales = {}
for product, qty in sales:
    total_sales[product] = total_sales.get(product, 0) + qty
print("5.", total_sales)


# 6. Word Length Grouping
words2 = ["cat", "dog", "elephant", "bat"]
length_group = {}
for word in words2:
    length = len(word)
    length_group.setdefault(length, []).append(word)
print("6.", length_group)


# 7. Employee Attendance Summary
attendance = {
    "Ravi": ["P", "A", "P"],
    "Neha": ["P", "P", "P"]
}
present_days = {}
for emp, records in attendance.items():
    present_days[emp] = records.count("P")
print("7.", present_days)


# 8. Character Index Mapping
s2 = "banana"
index_map = {}
for i, ch in enumerate(s2):
    index_map.setdefault(ch, []).append(i)
for ch in index_map:
    index_map[ch] = tuple(index_map[ch])
print("8.", index_map)


# 9. Merge Marks from Two Tests
test1 = {"Amit": 70, "Neha": 85}
test2 = {"Amit": 80, "Neha": 90}
merged_marks = {}
for name in test1:
    merged_marks[name] = (test1[name], test2[name])
print("9.", merged_marks)


# 10. Frequency-Based Word Filter
words3 = ["python", "java", "python", "c", "java"]
freq = {}
for word in words3:
    freq[word] = freq.get(word, 0) + 1

filtered_words = {word: count for word, count in freq.items() if count > 1}
print("10.", filtered_words)
