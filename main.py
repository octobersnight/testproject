from menu import resources, MENU

MONEY = 0.00
INSERT_COIN = 0.00


# TODO: Print report.
#   a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
def resource_report(money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    profit = money
    print("-----📋Resource Report-----\n" + f"🚰Water: {water} \n🥛Milk: {milk} \n☕Coffee: {coffee} \n💰Profit: ${profit}")


def display_resource():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("-----📋Resource Report-----\n" + f"🚰Water: {water} \n🥛Milk: {milk} \n☕Coffee: {coffee} \nPlease Select another beverage.")


# TODO: Check resources sufficient?
#   a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
#   b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#   not continue to make the drink but print: “Sorry there is not enough water.”
#   c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resource(selection):
    # local variables
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]

    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]

    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]

    match selection:
        case "e":
            if water < espresso_water:
                print("Low on water.")
                display_resource()
            if coffee < espresso_coffee:
                print("Low on coffee.")
                display_resource()
        case "l":
            if water < latte_water:
                print("Low on water.")
                display_resource()
            if milk < latte_milk:
                print("Low on milk.")
                display_resource()
            if coffee < latte_coffee:
                print("Low on coffee.")
                display_resource()
        case "c":
            if water < cappuccino_water:
                print("Low on water.")
                display_resource()
            if milk < cappuccino_milk:
                print("Low on milk.")
                display_resource()
            if coffee < cappuccino_coffee:
                print("Low on coffee.")
                display_resource()


# TODO:  Process coins.
#   a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
#   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel,
#   2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coin(coffee_type, coin):
    is_total_amount = True
    total_amount = 0.00
    total = 0.00
    coin_type = ""
    while is_total_amount:

        match coin_type:
            case "q":
                coin = 0.25
            case "d":
                coin = 0.10
            case "n":
                coin = 0.05
            case "p":
                coin = 0.01

        match coffee_type:
            case "e":
                if total == MENU["espresso"]["cost"]:
                    print("Thank you for your patron!")
                    is_total_amount = False
                elif total < MENU["espresso"]["cost"]:
                    total_amount = total_amount + coin
                    total = round(total_amount, 2)
                    print(f"Total: {total}")

        coin_type = input("Insert Coin: $0.25(Q), $0.10(D), $0.05(N), $0.01(P) ").lower()


# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
#   a. Check the user’s input to decide what to do next.
#   b. The prompt should show every time action has completed, e.g. once the drink is
#   dispensed. The prompt should show again to serve the next customer.
select_coffee = input("What would you like? espresso(E), latte(L), cappuccino(C): ").lower()


# TODO:  Turn off the Coffee Machine by entering “off” to the prompt.
#   a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#   the machine. Your code should end execution when this happens.
if select_coffee == "off":
    exit()
elif select_coffee == "e" or select_coffee == "l" or select_coffee == "c":
    check_resource(select_coffee)
else:
    exit()

process_coin(select_coffee, INSERT_COIN)


# TODO: Check transaction successful?
#   a. Check that the user has inserted enough money to purchase the drink they selected.
#   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#   program should say “Sorry that's not enough money. Money refunded.”.
#   b. But if the user has inserted enough money, then the cost of the drink gets added to the
#   machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#   c. If the user has inserted too much money, the machine should offer change.
#   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

# TODO: Make Coffee.
#   a. If the transaction is successful and there are enough resources to make the drink the
#   user selected, then the ingredients to make the drink should be deducted from the
#   coffee machine resources. E.g. report before purchasing latte:
#   Water: 300ml
#   Milk: 200ml
#   Coffee: 100g
#   Money: $0
#   Report after purchasing latte:
#   Water: 100ml
#   Milk: 50ml
#   Coffee: 76g
#   Money: $2.5
#   b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
