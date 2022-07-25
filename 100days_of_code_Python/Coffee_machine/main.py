from machine_data import MENU, resources

def report(resources_available, money_earned):
    print(f"water: {resources_available['water']}ml")
    print(f"milk: {resources_available['milk']}ml")
    print(f"coffee: {resources_available['coffee']}g")
    print(f"money: ${money_earned}")


def price_print(MENU):
    print(f"espresso: ${MENU['espresso']['cost']}")
    print(f"latte: ${MENU['latte']['cost']}")
    print(f"cappuccino: ${MENU['cappuccino']['cost']}")


def money_insert():
    quaters = int(input("how many quaters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickles?: "))
    pennies = int(input("how many pennies? "))
    money_total = quaters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return money_total


def money_check(money, choice, MENU):
    if money >= MENU[choice]['cost']:
        return True
    else:
        return False


def changes_cal(money_insert, choice, MENU):
    changes = round(money_insert - MENU[choice]['cost'], 2)
    return changes

def resources_left(choice_ingredients, resources_available):
    temp_resource = resources_available
    for item in choice_ingredients:
        temp_resource[item] -= choice_ingredients[item]
    return temp_resource

def check_resources(choice_ingredients):
    for item in choice_ingredients:
        if choice_ingredients[item] > resources_available[item]:
            print(f"Sorry,there is not enough {item}.")
            return False
    return True

def refill_resources(resources_available):
    for item in resources:
        resources_available[item] = resources[item]
    return resources_available

money_earned = 0
continue_serve = True
resources_available = {}
for item in resources:
    resources_available[item] = resources[item]

# TODO 1 print the choices that the user could choose from
while continue_serve:
    user_choice = input(" What would you like? (espresso/latte/cappuccino) \n Type 'price' to check for prices.\n"
                        " Type 'report' to see report. \n Type 'refill' to refill the machine. \n Type 'exit' to "
                        "exit.\n").lower()
    # TODO 2 if the user want to look up the report, print out the report
    if user_choice =='exit':
        continue_serve = False
    else:
        if user_choice == 'report':
            report(resources_available, money_earned)
        # TODO 3 if the user want to look up the price,print out the price
        elif user_choice == 'price':
            price_print(MENU)
        # TODO 4 if the user has successfully make a choice, check if the resources left
        #        are enough to make the coffee
        elif user_choice == 'refill':
             refill_resources(resources_available)
        else:
            if check_resources(MENU[user_choice]['ingredients']):
                print("Please insert coins.")
                money_get = money_insert()
                if not money_check(money_get, user_choice, MENU):
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    money_earned += MENU[user_choice]['cost']
                    resources_available = resources_left(MENU[user_choice]['ingredients'], resources_available)
                    print(f"Here is ${changes_cal(money_get, user_choice, MENU)} in change.")
                    print(f"Here is your {user_choice} ☕️.Enjoy!")


# TODO 5 Then let the user insert coinscheck if the money inserted is enough to pay for the coffee.
#        if it's enough to pay for the coffee, then make the coffee and return the changes, and refresh coffee machine
#        inventories, sum up the money that the coffee machine has earned; else if the money is not
#        enough to pay, refund the user the money.

# TODO 6 before make coffee, check if there still has enough resources to make the coffee
