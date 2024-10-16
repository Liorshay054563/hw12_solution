# start - Homework 12 - loop
# 6

n: int = int(input("Enter a number:"))

for i in range(n, 1 - 1, -1):
    print(i, end=" ")
print()

# 7
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

if num2 > num1:
    for num in range(num1, num2):
        if num % 2 == 0:
            print(num, end=" ")
else:
    for num in range(num2, num1):
        if num % 2 == 0:
            print(num, end=" ")

# 8
a: int = int(input("Enter a positive number:"))

for i in range(1, a + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=" ")
print()

# 9
b: int = int(input("Enter a positive number:"))

for i in range(1, b + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()
