from menu import MENU

def resource_check(water, milk, coffee, type):
    if MENU[type]['ingredients']['water'] > water:
        print("Sorry there is not enough water.")
        return False
    elif MENU[type]['ingredients']['milk'] > milk:
        print("Sorry there is not enough milk.")
        return False
    elif MENU[type]['ingredients']['coffee'] > coffee:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennis = int(input("How many pennis?: "))
    return quarters*0.25 + dimes*0.1 + nickles*0.05 + pennis*0.01

def transaction(coins, type):
    if coins >= MENU[type]['cost']:
        print(f"Here is your ${round((coins - MENU[type]['cost']), 3)} in change.")
        return True
    else:
        print("Sorry there is no enough money. Money Refunded")
        return False

def make_coffee(water, milk, coffee, money, type):
    print(f"Here is your {type}. Enjoy!")
    water -= MENU[type]['ingredients']['water']
    milk -= MENU[type]['ingredients']['milk']
    coffee -= MENU[type]['ingredients']['coffee']
    money += MENU[type]['cost']
    return water, milk, coffee, money

def report(water, milk, coffee, money):
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def coffee_machine(water, milk, coffee, money):
    keep_processing = True

    while keep_processing == True:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if action == "espresso" or action == "latte" or action == "cappuccino":
            sufficient_resource = resource_check(water, milk, coffee, action)
            if sufficient_resource:
                coins = process_coins()
                sufficient_money = transaction(coins, action)
                if sufficient_money:
                    water, milk, coffee, money = make_coffee(water, milk, coffee, money, action)
            keep_processing = False
        
        elif action == "off":
            return

        elif action == "report":
            report(water, milk, coffee, money)    
        
    coffee_machine(water, milk, coffee, money)

coffee_machine(300, 200, 100, 0)