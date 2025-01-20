menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

# TODO: 1. print the report
def report():
    print(f"water:{resources["water"]}\nmilk:{resources["milk"]}\ncoffee:{resources["coffee"]}")
# TODO:3. make the selected coffee type
def baking_beans(kaffe):
    print(f"Here's your {kaffe} ,have a nice Day")


# TODO: 2. take the choice of coffee from user

def coffee_type():
    make_coffee=False

    choice=input("What would you like? (espresso/latte/cappuccino):")
    if menu[choice]["ingredients"]["milk"]<=resources["milk"]:
        if menu[choice]["ingredients"]["water"]<=resources["water"]:
            if menu[choice]["ingredients"]["coffee"]<=resources["coffee"]:
                price=menu[choice]["cost"]
                money=float(input(f"The cost of coffee is {price}\n Please enter coins worth Rupees {price} to continue "))
                if money==price:
                    make_coffee=True
                else:
                    make_coffee=False

    if make_coffee==True:
        baking_beans(choice)
    else:
        print("Sorry less ingredients present please refill or choose another coffee type")
        coffee_type()

report()
coffee_type()
