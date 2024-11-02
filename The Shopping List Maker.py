# Objective: The aim of this assignment is to create a program that helps users make a shopping list.
# Task 1: Write a function that lets the user add items to a list.

grocery_list =  []

def add_single_item():                                                                                    #defining a function to add a single item to the list
    new_item = input("\nEnter the item you'd like to add to the list: ")
    grocery_list.append(new_item)

def add_multi_item():                                                                                     #defining a function to add multiple items to the list
    items = int(input("\nEnter how many items you'd like to add to the list: "))    
    for item in range(items):
        item = input("\nEnter the item you'd like to add the list: ")
        grocery_list.append(item)



# Task 2: Include a function to remove items from the list.

def remove_single_item():                                                                                #defining a function to remove a single item from the list
    print(f"\nThe current grocery list is: {grocery_list}")
    item_remove = input("\nEnter the item you'd like to remove: ")
    grocery_list.remove(item_remove)

def remove_multi_item():                                                                                 #defining a function to remove multiple items from the list
    print(f"\nThe current grocery list is: \n{grocery_list}")
    delete_item = int(input("\nEnter the number of items you wish to remove: "))
    for delete in range(delete_item):
        print(f"\n{grocery_list}")
        delete = input("\nEnter the item you'd like to remove: ")
        grocery_list.remove(delete)

#Task 3: Add a function that prints out the entire list in a formatted way.

def make_grocery_list():                                                                                #function that will cycle through some choices allowing the user to view the grocery list, add or remove items from the list, or to print the list when finished
    while True:                                                                                         #infinite "while" loop to cycle through the choices until the user is finished
        print("\nWelcome to the Grocery List Maker, please select one:")
        print("1. View Current List")
        print("2. Add single item to list")
        print("3. Add multiple items to list")                                                          #print statements telling the user their choices
        print("4. Remove single item from list")
        print("5. Remove multiple items from list")
        print("6. Exit and print list")
        user_choice = input("Enter you selection (1-6): ")                                              #variable set to "input" to get the user's choice 

        if user_choice == "1":
            print(f"\n{grocery_list}")
        elif user_choice == "2":
            add_single_item()
        elif user_choice == "3":
            add_multi_item()                                                                            #series of "if" and "elif" statements defining what should happen depending on the users choice
        elif user_choice == "4":
            remove_single_item()
        elif user_choice == "5":
            remove_multi_item()
        elif user_choice == "6":
            print("\nYour grocery list is: ")                                                          #print statement to give the user their finalized list
            for grocery in grocery_list:                                                               #"for" loop to print the list in a more formatted manner
                print(grocery)
            break                                                                                      #break statement to end the "while" loop                                       
        else:
            print("You have entered an invalid choice. Please enter a number 1 through 6.")            #else statement informing the user they have made an invalid chocie

make_grocery_list()                                                                                    #running the function 





    


