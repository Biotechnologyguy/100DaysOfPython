from data import MENU, resources

machine_is_on = True
money = 0


# creating the function to print the report
def print_report():
    for resource in resources:
        print(f"{resource} : {resources[resource]}")
    print(f"Money : ${money}")


def resources_are_sufficient(item_name):
    item_ingredients = MENU[item_name]["ingredients"]
    for ingredient_name in item_ingredients:
        if not resources[ingredient_name] >= item_ingredients[ingredient_name]:
            print(f"Sorry there is not enough {ingredient_name}.")
            return False
    return True


def process_coins(quarters_coins, dimes_coins, nickles_coins, pennies_coins):
    return quarters_coins * 0.25 + dimes_coins * 0.1 + nickles_coins * 0.05 + pennies_coins * 0.01


def make_coffee(user_drink):
    item_ingredients = MENU[user_drink]["ingredients"]
    for ingredient_name in item_ingredients:
        resources[ingredient_name] -= item_ingredients[ingredient_name]
    print(f"Here is your {user_drink}☕. Enjoy!")


while machine_is_on:
    user_wants = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_wants == "report":
        print_report()
    elif user_wants == "off":
        machine_is_on = False
    elif user_wants == "latte" or user_wants == "espresso" or user_wants == "cappuccino":
        if resources_are_sufficient(user_wants):
            print("Please insert coins.")
            quarters = float(input("How many quarters? : "))
            dimes = float(input("How many dimes? : "))
            nickles = float(input("How many nickles? : "))
            pennies = float(input("How many pennies? : "))
            coin_value = process_coins(quarters, dimes, nickles, pennies)
            drink_cost = MENU[user_wants]["cost"]
            if coin_value >= drink_cost:
                money += drink_cost
                make_coffee(user_wants)
                if coin_value > drink_cost:
                    change = round(coin_value - drink_cost, 2)
                    print(f"Here is ${change} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Please select appropriate option")
