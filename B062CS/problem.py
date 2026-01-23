num1 = [2, 6, 8]
num2 = [1, 2, 7, 8, 9]

i = j = 0
merged = []

while i < len(num1) and j < len(num2):
    if num1[i] < num2[j]:
        merged.append(num1[i])
        i += 1
    else:
        merged.append(num2[j])
        j += 1


merged.extend(num1[i:])
merged.extend(num2[j:])

print(merged)
