# Make 3 hot flavours.
# 1. Espresso (50ml Water, 18g coffee, $1.50)
# 2. Latte (200ml Water, 24g coffee, 150ml milk, $2.50)
# 3. Cappuccino (250ml water, 24g coffee, 100ml milk, $3.00)
# Total amount of water  = 300ml
#                 milk   = 200ml
#                 coffee = 100g
from coffee_art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MACHINE_MONEY = 0

# Coin operated
# penny   = $0.01
# dime    = $0.10
# nickel  = $0.50
# quarter = $0.25

# TODO 1. Print report
#      2. Check resources sufficient?
#      3. Process coins
#      4. Check transaction successful?
#      5. Make coffee.


def show_report():
    """Print the amount of resources left"""
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Money: ${MACHINE_MONEY}")

def check_resources(choice):
    k=0
    for key in MENU:
        if key == choice:
            ingredient = MENU[key]['ingredients']
            for new_key in resources:
                if new_key not in ingredient:
                    ingredient[new_key] = 0
                if ingredient[new_key] > resources[new_key]:
                    print(f"Sorry, there is not enough {new_key}")
                    k = 1
                    break

    return k

def enter_money():
    """asks the user to enter the amount of money
    and check whether it is sufficient or not"""
    print("Please insert coins.")
    qua = int(input("How many quarters?: "))
    dim = int(input("How many dimes?: "))
    nic = int(input("How many nickels?: "))
    pen = int(input("How many pennies?: "))
    tot = qua * 0.25 + dim * 0.1 + nic * 0.05 + pen * 0.01
    return tot


def check_money(amt, choice):
    """Check the transaction if the amount of
    money entered is sufficient for the coffee """
    global MACHINE_MONEY
    price = MENU[choice]['cost']
    change = round((amt - price),2)
    if change >= 0:
        MACHINE_MONEY += price
    return change


def make_coffee(choice):
    """depending on the user choice this function
    makes coffee and does the necessary calculations"""
    ingredient = MENU[choice]['ingredients']
    for key in resources:
        resources[key] -= ingredient[key]


is_working = True  # variable to check whether the coffee machine is working
print(logo)
while is_working:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino}: ").lower()

    list_of_coffee = []
    for keys in MENU:
        list_of_coffee.append(keys)

    if coffee_choice == 'off':
        is_working = False
    elif coffee_choice == 'report':
        show_report()
    else:
        if coffee_choice not in list_of_coffee:
            print("System does not understand")
        else:
            f = check_resources(coffee_choice)
            if f == 1:
                continue
            else:
                money = enter_money()
                change = check_money(money,coffee_choice)
                if change < 0:
                    print("Sorry that's not enough money. Money refunded")
                    continue
                else:
                    print(f"Here is ${change} dollars in change.")
                    make_coffee(coffee_choice)
                    print(f"Here is your {coffee_choice}. Enjoy!")

