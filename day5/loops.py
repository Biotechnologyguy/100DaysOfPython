fruits = ["Apple", "Pear", "Peach"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# for loops with range() function
# here else will get executed once loop is over
total = 0
for num in range(1, 101):
    total += num
else:
    print(f"sum is {total}")

# Program to get sum of all even nums
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for even_num in range(2, target + 1, 2):
    total += even_num
else:
    print(total)


