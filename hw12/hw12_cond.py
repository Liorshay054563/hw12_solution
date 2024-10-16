# start - Homework 12
# 1
num_input: int = int(input("Enter a number:"))

if num_input > 10:
    print(f"The diff is -{num_input - 10}")
else:
    print(f"{num_input} * 10 = {num_input * 10}")

# 2
num2_list: list[int] = []
for i in range(3):
    num2_input: int = int(input("Enter a number:"))
    num2_list.append(num2_input)
if sum(num2_list) > 100:
    print(sum(num2_list))
else:
    print("sum is under 100")

# 3 bonus
x: float = float(input("Enter a number:"))
Y: float = float(input("Enter a number:"))

# 4
age: int = int(input("Enter your age:"))

if 0 < age <= 120:
    print("age")
else:
    print('wrong age')
# 5
three_digit: int = int(input("Enter a number:"))
if three_digit > 100:
    three_digit = (three_digit // 10)
    middel = three_digit % 10
    print(middel)
