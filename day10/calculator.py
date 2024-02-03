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


def calculator():
    continue_operation = True
    num1 = int(input("What's the first number? : "))
    for key in operations:
        print(key)
    while continue_operation:
        operation_symbol = input("Pick an operation : ")
        num2 = int(input("What's the next number? : "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a "
                                   f"new calculation : ") == "y":
            num1 = answer
        else:
            continue_operation = False
            calculator()


calculator()
