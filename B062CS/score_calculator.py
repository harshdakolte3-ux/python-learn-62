students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

total_marks = sum(
    (mark + 5)
    for student in students
    if sum(student["marks"]) / len(student["marks"]) >= 60
    for mark in student["marks"]
)

print(total_marks)
