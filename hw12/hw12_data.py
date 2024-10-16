# start
# 11
num_negative: int = 0
SENTINEL = 0

while True:
    num: int = int(input("Enter a number:"))
    if SENTINEL == num:
        break
    if num > 0:
        continue
    num_negative += num
print(f"The sum of all the negative number is {num_negative} ")
import statistics

# 12
list10: list[int] = []
for i in range(10):
    x: int = int(input("Enter number"))
    list10.append(x)
print(f"{list10[::-1]}")

# 13
list_prime: list[int] = []
SENTINEL = 0
while True:
    x: int = int(input("Enter a number:"))
    if SENTINEL == x:
        break
    if x < 1:
        continue
    else:
        if x == 1:
            continue
        elif x == 2:
            list_prime.append(x)
        elif x % 2 == 0:
            continue
        else:
            divider: int = 3
            found_divider: bool = False
            while divider <= x ** 0.5 + 1:
                if x % divider == 0:
                    found_divider = True
                    break
                divider += 2
            if not found_divider:
                list_prime.append(x)
print(list_prime)

# 14

above_avg: int = 0
num_avg: list[int] = [int(input("Enter a number")) for i in range(5)]
for num in num_avg:
    if num > statistics.mean(num_avg):
        above_avg += 1
print(f"The avg is {statistics.mean(num_avg)}, and {above_avg} numbers above the avg")

# 15
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
haluka = 0

if num1 > num2:
    while num1 >= num2:
        num1 -= num2
        haluka += 1
else:
    while num2 >= num1:
        num2 -= num1
        haluka += 1
print(haluka)
