#coding:utf-8

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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_ressources_suffisant (order_ingredients):
    """ Return true when orders can be made or False when Ingredients are not enough """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry , there is not enough {item}")
            is_enough = False
    return is_enough


def process_coin ():
    """
    Return the total of coins
    """
    print("Insert your coins")
    quarters = int(input("how many quarters: ")) * 0.25
    dimes = int(input("how many dimes: ")) * 0.1
    nickles = int(input("how many nickles: ")) * 0.05
    pennies = int(input("how many pennies: ")) * 0.01
    total_coin = quarters + dimes + nickles + pennies
    return total_coin

def is_transaction_successful (money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print('''You don't have enough money. Money refounded''')
        return False


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients [item]
    print(f" here is your drink {drink_name} ☕ ")



is_on = True
while is_on:
    choice = input('''What would you like: espresso/latte/cappuccino or "r" for report: \n''')
    if choice == "off":
        is_on = False
    elif choice == "r":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        if is_ressources_suffisant(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])



