from art import logo

print(logo)


# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def sub(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number? : "))
num2 = int(input("What's the Second number? : "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation from above line : ")

answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
