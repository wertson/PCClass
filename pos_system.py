
def main():
    cb = 1
    pizza = 2
    soda = 3
    quit_program = 4
    choice = 0

    while choice != quit_program:

        choice = int(input('What would you like to add to your order? \n 1. Cheeseburger \n 2. Pizza \n 3. Soda \n = = = = = = = = = = = = = = = = \n 4. Quit \n'))

        if choice == cb:
            cheeseburger()
        elif choice == pizza:
            pizza()
        elif choice == soda:
            soda()
        else:
            print("Error: Invalid Selection.")

        return





def cheeseburger():
    main_menu = ""
    
    choice_temperature = input("How would you like it cooked? \n 1. Rare \n 2. Medium Rare \n 3. Medium \n 4. Medium Well \n 5. Well Done \n")
    
    choice_cheese = input("What kind of cheese would you like? \n 1. American \n 2. Swiss \n 3. Cheddar \n")

    choice_toppings_cb = input(" Any toppings? \n 1. Lettuce \n 2. Tomatoes \n 3. Bacon \n 4. Onions \n")

    main_menu = input("Would you like to add more food to your order? \n y = yes \n n = no ")

    if main_menu == "yes" or "y":
        main()
    else:
        print("You ordered a Cheeseburger cooked", + choice_temperature, "with", + choice_cheese, "cheese, with", + choice_toppings_cb) 
def pizza():
    small = s
    medium = m
    large = l
    size = input("What is the size of the pizza you would like to order? \n s = Small \n m = Medium \n l = Large")
    toppings = input("Which toppings would you like to add to your pizza? \n 1. Extra Cheese \n 2. Pepperoni \n 3. Peppers \n 4. Onions \n")
def soda():
    soda_choice = input("What would you like for a Soda?")
    
    
main()
