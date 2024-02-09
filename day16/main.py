from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True
while machine_is_on:
    user_wants = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_wants == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_wants == "off":
        machine_is_on = False
    else:
        menu_item = menu.find_drink(user_wants)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
