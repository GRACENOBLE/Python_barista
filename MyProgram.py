COFFEE = 8

CAPPUCCINO = 9

FRESCO = 10

COKTAIL = 11

menu = [ COFFEE , CAPPUCCINO , FRESCO , COKTAIL ]

name_menu = [ "COFFEE" , "CAPPUCCINO" , "FRESCO" , "COKTAIL" ]

name = input("\n\nHello, what is your name?\n")#asking user their name.

print("\n\nHello " + name + ", welcome to the coffee shop, this is our menu:\n")#showing them the menu.

for string in name_menu:
    print (string)

orders = int(input("\nYou can make a single order or you can make multiple orders.\nHow many orders would you like to make?\n"))#asking the number of orders.

def one_order():#function that handles the case that the user makes one order.
    the_one_order = int(input("\nWhat would you like to have? Please select one item.\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))

    number = int (input("\nHow many of those will you take?\n"))

    if the_one_order == 1:
        ctotal = menu[the_one_order - 1] * number#Using a list index corresponding to the user input to select a list item
        print("\nOkay " + str(name) + " your Coffe will be ready in about five minutes." + "\nThat'll be " + str(ctotal) + "$\n")
    elif the_one_order == 2:
        cptotal = menu[the_one_order - 1] * number
        print("\nOkay " + str(name) + " your Cappuccino will be ready in about five minutes." + "\nThat'll be " + str(cptotal) + "$\n")
    elif the_one_order == 3:
        ftotal = menu[the_one_order - 1] * number
        print("\nOkay " + str(name) + " your Fresco will be ready in about five minutes." + "\nThat'll be " + str(ftotal) + "$\n")
    elif the_one_order == 4:
        cototal = menu[the_one_order - 1] * number
        print("\nOkay " + str(name) + " your Coktail will be ready in about five minutes." + "\nThat'll be " + str(cototal) + "$\n")
    else:
        print("\nWe dont have that yet.\n")
    exit()

def two_orders():#function that handles the case that the user makes 2 orders.
    first_order = int(input("\nPlease select a first order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking first order

    first_order_number = int(input("\nHow many of those would you like?\n"))#taking a certain number of first orders

    second_order = int(input("\nPlease select a second order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking second order
    
    second_order_number = int(input("\nHow many of those would you like?\n"))#Taking a certain number of second orders

    total_for_two = (menu[first_order - 1] * first_order_number) + (menu[second_order -1] *second_order_number)#doing the maths for the two orders made from the menu using the list

    print("\nThat will cost you a total of " + str(total_for_two) +"$\n")#telling the user how much he/she is charged

def three_orders():#function that handles the case that the user makes 3 orders.
    first_order = int(input("\nPlease select a first order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking first order

    first_order_number = int(input("\nHow many of those would you like?\n"))#taking a certain number of first orders

    second_order = int(input("\nPlease select a second order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking second order
    
    second_order_number = int(input("\nHow many of those would you like?\n"))#Taking a certain number of second orders

    third_order = int(input("\nPlease select a third order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking third order
    
    third_order_number = int(input("\nHow many of those would you like?\n"))#Taking a certain number of third orders

    total_for_three = (menu[first_order - 1] * first_order_number) + (menu[second_order -1] *second_order_number) + (menu[third_order - 1] * third_order_number)#doing the maths for the three orders made from the menu using the list

    print("\nThat will cost you a total of " + str(total_for_three) +"$\n")#telling the user how much he/she is charged
    exit()

def four_orders():#function that handles the case that the user makes 4 orders.
    first_order = int(input("\nPlease select a first order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking first order

    first_order_number = int(input("\nHow many of those would you like?\n"))#taking a certain number of first orders

    second_order = int(input("\nPlease select a second order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking second order
    
    second_order_number = int(input("\nHow many of those would you like?\n"))#Taking a certain number of second orders

    third_order = int(input("\nPlease select a third order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking third order
    
    third_order_number = int(input("\nHow many of those would you like?\n"))#Taking a certain number of third orders

    fourth_order = int(input("\nPlease select a fourth order:\n1.Coffee-------8$\n2.Cappuccino---9$\n3.Fresco------10$\n4.Coktail-----11$\n"))#Taking fourth order
    
    fourth_order_number = int(input("\nHow many of those would you like?\n"))#Taking a certain number of fourth orders

    total_for_four = (menu[first_order - 1] * first_order_number) + (menu[second_order -1] *second_order_number) + (menu[third_order - 1] * third_order_number) + (menu[fourth_order - 1] * fourth_order_number)#doing the maths for the three orders made from the menu using the list

    print("\nThat will cost you a total of " + str(total_for_four) +"$\n")#telling the user how much he/she is charged
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
    print("Sorry we can only accept a maximum of four orders at a time")
    exit()#EXITING THE PROGRAM