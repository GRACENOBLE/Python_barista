name = input("\n\nHello, what is your name?\n")

choice =int (input("Hello, welcome to the coffee shop, may i take your order?\t\t PLEASE SELECT A NUMBER FROM THE LIST BELOW\n1.Coffee------8$\n2.Cappuccino-------9$\n3.Fresco------10\n4.Coktail-----11\n\n"))

if choice == 1:
    print("Okay " + name + " your Coffe will be ready in about five minutes.")
elif choice == 2:
    print("Okay " + name + " your Cappuccino will be ready in about five minutes.")
elif choice == 3:
    print("Okay " + name + " your Fresco will be ready in about five minutes.")
elif choice == 4:
    print("Okay " + name + " your Coktail will be ready in about five minutes.")
else:
    print("We dont have that yet.")