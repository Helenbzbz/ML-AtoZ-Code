from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money_register = MoneyMachine()
coffee_menu = Menu()

continue_order = True

while continue_order:
    action = input(f"What would you like? {coffee_menu.get_items()}: ").lower()

    if action == "off":
        break
    elif action == "report":
        coffee_machine.report()
        money_register.report()
    else:
        item = coffee_menu.find_drink(action)
        can_make = coffee_machine.is_resource_sufficient(item)
        if can_make:
            enough_money = money_register.make_payment(item.cost)
            if enough_money:
                coffee_machine.make_coffee(item)

