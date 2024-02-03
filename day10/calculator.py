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
for key in operations:
    print(key)
operation_symbol = input("Pick an operation from above line : ")
num2 = int(input("What's the Second number? : "))
first_answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")
continue_operation = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit : ") == "y"
while continue_operation:
    operation_symbol = input("Pick another operation : ")
    num3 = int(input("What's the next number? : "))
    second_answer = operations[operation_symbol](first_answer, num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    first_answer = second_answer
    continue_operation = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to exit : ") == "y"

