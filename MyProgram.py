name = input("\n\nHello, what is your name?\n")#asking user their name.

print("\n\nHello " + name + ", welcome to the coffee shop, this is our menu\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11&\n\n")#showing them the menu.

orders = int(input("How many orders would you like to make?\n"))#asking the number of orders.

def one_order():#function that handles the case that the user makes one order.
    one_order = int(input("\nWhat would you like to have? Please select one item.\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))

    number = int (input("\nHow many of those will you take?\n"))

    COFFEE = 8

    CAPPUCCINO = 9

    FRESCO = 10

    COKTAIL = 11

    if one_order == 1:
        ctotal = COFFEE * number
        print("\nOkay " + str(name) + " your Coffe will be ready in about five minutes." + "\nThat'll be " + str(ctotal) + "$\n")
    elif one_order == 2:
        cptotal = CAPPUCCINO * number
        print("\nOkay " + str(name) + " your Cappuccino will be ready in about five minutes." + "\nThat'll be " + str(cptotal) + "$\n")
    elif one_order == 3:
        ftotal = FRESCO * number
        print("\nOkay " + str(name) + " your Fresco will be ready in about five minutes." + "\nThat'll be " + str(ftotal) + "$\n")
    elif one_order == 4:
        cototal = COKTAIL * number
        print("\nOkay " + str(name) + " your Coktail will be ready in about five minutes." + "\nThat'll be " + str(cototal) + "$\n")
    else:
        print("\nWe dont have that yet.\n")
    exit()

def two_orders():#function that handles the case that the user makes 2 orders.
    print("comming soon")
    exit()

def three_orders():#function that handles the case that the user makes 3 orders.
    print("comming soon")
    exit()

def four_orders():#function that handles the case that the user makes 4 orders.
    print("comming soon")
    exit()

if orders == 1:#Calling respective functions basing on the number of orders made.
    one_order()
elif orders == 2:
    two_orders()
elif orders == 3:
    three_orders()
elif orders == 4:
    four_orders()
else:
    ptint("Sorry we can only accept a maximum of four orders at a time")
    exit()