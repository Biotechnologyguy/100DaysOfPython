from data import MENU, resources

machine_is_on = True


# creating the function to print the report
def print_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")


while machine_is_on:
    user_wants = input("What would you like? (espresso/latte/cappuccino): ")
    if user_wants.lower() == "report":
        print_report()
    elif user_wants.lower() == "off":
        machine_is_on = False


