##Write a script that converts numbers to characters using map function.##
def num_char(num):
    return chr(num)

numbers = [72, 69, 76, 76, 79]
characters = map(num_char, numbers)

print(list(characters))

##(2) WAP script that gives the ASCII value of characters using map function
def ascii(char):
    return ord(char)

characters = ['A', 'B', 'C', 'D']
ascii_val = map(ascii, characters)

print(list(ascii_val))

##3) Write a user defined function that square all the numbers in a list. Use a map function.
def sq(num):
    return num**2

nums = [2, 4, 6, 8]
square = map(sq, nums)

print(list(square))


##(4) Write a user defined function to filter and print only the vowels in a given list and
def sq(num):
    return num**2

nums = [2, 4, 6, 8]
square = map(sq, nums)

print(list(square))



##(5) Write a user defined function to filter out even and odd number in a given list and
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Even numbers
even = list(filter(lambda n: n % 2 == 0, mylist))
print("Even numbers:", even)

# Odd numbers
odd = list(filter(lambda n: n % 2 != 0, mylist))
print("Odd numbers:", odd)


##(6) Write a script to calculate the factorial of a number using reduce function.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
