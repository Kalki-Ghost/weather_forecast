from data import MENU, profit, resources


def report():
    print(f'Water : {resources["water"]}ml')
    print(f'Milk : {resources["milk"]}ml')
    print(f'Coffee : {resources["coffee"]}g')
    print(f'Money : ${profit}')


def preparation(type_coffee):
    coffee_ingredients = MENU[type_coffee]['ingredients']

    if coffee_ingredients["water"] > resources["water"]:
        print("Sorry there  is not enough water.Money is refunded.")
        return False
    elif coffee_ingredients != "espresso" and coffee_ingredients["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.Money is refunded.")
        return False
    elif coffee_ingredients["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.Money is refunded.")
        return False
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    return True


def money_calculation():
    print("Please insert coins.")
    quarters = int(input('How many quarters?'))
    dimes = int(input('How many dimes?'))
    nickles = int(input('How many nickles?'))
    pennies = int(input('How many pennies?'))
    amount = 0.25 * quarters + .1 * dimes + .05 * nickles + .01 * pennies
    return amount


def money_deduction(amount, type_coffee):
    remaining_amount = amount - MENU[type_coffee]['cost']
    if remaining_amount < 0:
        print("Sorry there is not enough money.")
        return False

    elif remaining_amount == 0:
        return
    else:
        print(f"Here is ${round(remaining_amount, 2)} in change.")
        return True


try:
    while True:
        require = input("What would you like?(espresso/latte/cappuccino):").lower()
        if require == 'report':
            report()
            continue
        else:
            money = money_calculation()
            money_flag = money_deduction(money, require)
            if not money_flag:
                continue
            flag = preparation(require)
            if flag:
                profit += MENU[require]['cost']

                print(f"Here is your {require}🍵 Enjoy!")

except KeyboardInterrupt:
    print("\nMachine is off.")
except KeyError:
    print("You enter wrong coffee.")

