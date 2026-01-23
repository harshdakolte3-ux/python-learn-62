num1 = [2, 6, 8]
num2 = [1, 2, 7, 8, 9]

merged = sorted(num1 + num2)
print(merged)



arr = [1, 3, 5, 6, 7]
number = 3

for i in range(len(arr)):  #checks elements
    if arr[i] >= number: #3>=i(all numbers)
        print(i)   
        break


nums = [2, 3, 3, 5, 7, 8, 9] 
target = 12
seen = {}
for i, num in enumerate(nums):
    need = target - num
    if need in seen:
        print([seen[need] + 1, i+1]) 
        break
    seen[num] 



    def main():
    n= [2,4,2,3,2,4,5,6,7,4,3,6,2,4,6]
    nc2 = n.count(2)
    nc3 = n.count(3) 
    nc4 = n.count(4)
    nc5 = n.count(5)
    nc6 = n.count(6)
    nc7 = n.count(7) 
    majority = max(nc2, nc3, nc4, nc5, nc6, nc7)
    if majority == nc2:
        print("Majority element is 2")
    elif majority == nc3:
        print("Majority element is 3")
    elif majority == nc4:
        print("Majority element is 4")
    elif majority == nc5:
        print("Majority element is 5")
    elif majority == nc6:
        print("Majority element is 6")
    else:
        print("Majority element is 7")
        
if __name__ == "__main__":
    main()

