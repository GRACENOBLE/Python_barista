name = input("\n\nHello, what is your name?\n")

print("\n\nHello " + name + ", welcome to the coffee shop, this is our menu\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11&\n\n")

orders = int(input("How many orders would you like to make?\n"))

def one_order():
    print("comming soon")
    exit()

def two_orders():
    print("comming soon")
    exit()

def three_orders():
    print("comming soon")
    exit()

def four_orders():
    print("comming soon")
    exit()

if orders == 1:
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


"""COFFEE = 8

CAPPUCCINO = 9

FRESCO = 10

COKTAIL = 11

number = int (input("\nHow many of those will you take?\n"))

if choice == 1:
    ctotal = COFFEE * number
    print("\nOkay " + str(name) + " your Coffe will be ready in about five minutes." + "\nThat'll be " + str(ctotal) + "$\n")
elif choice == 2:
    cptotal = CAPPUCCINO * number
    print("\nOkay " + str(name) + " your Cappuccino will be ready in about five minutes." + "\nThat'll be " + str(cptotal) + "$\n")
elif choice == 3:
    ftotal = FRESCO * number
    print("\nOkay " + str(name) + " your Fresco will be ready in about five minutes." + "\nThat'll be " + str(ftotal) + "$\n")
elif choice == 4:
    cototal = COKTAIL * number
    print("\nOkay " + str(name) + " your Coktail will be ready in about five minutes." + "\nThat'll be " + str(cototal) + "$\n")
else:
    print("\nWe dont have that yet.\n")"""