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
    print(f"water:{resources['water']}\nmilk:{resources['milk']}\ncoffee:{resources['coffee']}")
    for i in range(0,5):
        print("\n")
#TODO:4 To reorder coffee
def re_order():
    reorder=input("Type'menu' button to order another coffee else type 'off' to turn off the machine: ")
    if reorder=='menu':
        report()
        coffee_type()
    elif reorder=='off':
        print("turning off, Good bye")
        for i in range(0,20):
            print("\n")
        
    else:
        print("Invalid choice, make sure you type the correct response")
        re_order()
        for i in range(0,20):
            print("\n")
# TODO:3. make the selected coffee type
def baking_beans(kaffe):
    print(f"Here's your {kaffe} ,have a nice Day")
    print("""        (  )   (   )  )
             ) (   )  (  (
             ( )  (    ) )
            _____________
           <_____________> ___
           |             |/ _ \
           |               | | |
           |               |_| |
           |             |\___/
            \___________/    
 """)
    resources["water"]-= menu[kaffe]["ingredients"]["water"]
    resources["milk"]-=menu[kaffe]["ingredients"]["milk"]
    resources["coffee"]-=menu[kaffe]["ingredients"]["coffee"]
    re_order()
    

     
    
    

# TODO: 2. take the choice of coffee from user
def coffee_type():
    refill=1
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
        refill+=1
        if refill<3:
            print("Sorry less ingredients present please refill or choose another coffee type")
            for i in range(0,20):
                print("\n")
            coffee_type()
        else:
            print("You cannot have any coffee items because of less ingredients.Please refill. ")
            for i in range(0,20):
                print("\n")
report()
coffee_type()
