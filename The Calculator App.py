# Objective: The aim of this assignment is to vuild a basic claculator that can perform addiction, subtraction, multiplication, and, division.
# Task 1: Create functions for each arithmetic operation.

def add_func(a, b):                                  #defining a function called add_func
    sum_number = a + b                               #setting up the function to add two numbers
    print(sum_number)                                #print statement to show the outcome of the function

def subtract_func(a, b):                             #defining a function called subtract_func
    sub_number = a - b                               #setting up the function to subtract one number from the other
    print(sub_number)                                #print statement to show the outcome of the function

def multiply_func(a, b):                             #defining a function called multiply_func
    multi_number = a * b                             #setting up the function to multiply two numbers together
    print(multi_number)                              #print statement to show the outcome of the function

def divide_func(a, b):                               #defining a function called divide_func
    div_number = a / b                               #setting up the funciton to divide one number from the other
    print(div_number)                                #print statement to show the outcome of the funciton

# Task 2: Use inputs to ask the user what operation they want 
#to perform, and what numbers they want to use.

number1 = float(input("\nEnter the first number you'd like to use in the calculation: "))                             #defining a variable to be the first number used in the calculation. Setting it to be "float", and making it user input

number2 = float(input("\nEnter the second number you'd like to use in the calculation:"))                             #defining a variable to be the second number in the calculation. Setting it to "float", and making it an input from the user

calculation = input("Enter which calculation you would like to perform: [add, subtract, multiply, divide] ")          #defining a new variable to be ask the user what calculation they would like to use
if calculation == "add":                                                                  
    calculation = add_func(number1, number2)                                                                          #setting up an "if" statement to carry out the chosen calculation using the numbers previously provided by the user
elif calculation == "subtract":
    calculation = subtract_func(number1, number2)
elif calculation == "multiply":
    calculation = multiply_func(number1, number2)
elif calculation == "divide":
    calculation = divide_func(number1, number2)
else:
    print("\nThe calculation you've entered is not recognized.")                                                     #else statement that tells the user they have entered an unrecognized calculation

# Task 3: Ensure your code can handle division by zero and other potential errors. So if you
#divide by 0, there is error handling set up to prevent an error from showing up in the console

number1 =input("\nEnter the first number you'd like to use in the calculation: ")    

while True:                                                                                                        #infinite "while" loop to cycle as many times as needed until  a number is entered
    if number1.isnumeric():                                                                                        #"if" statement ascertaining if "number1" is a numeric value
        number1 = float(number1)                                                                                   #if "number1" is a numeral then it is converted to "float"
        break                                                                                                      #break statement to end the "while" loop
    else:                                                                                                          #"else" statement in case "number1" isnt a numeral
        print("\nYou have entered a non-numeric character, please enter a number.")                                      #print statement letting the user know the input was non-numerical
        number1 = input("\nEnter the first number you'd like to use in the calculation: ")                         #another input statement asking the user for "number1".
                                 

number2 =input("\nEnter the second number you'd like to use in the calculation:") 

while True:                                                                                                        #did the same thing for "number2" as for "number1" above
    if number2.isnumeric():
        number2 = float(number2)
        break
    else:
        print("\nYou have entered a non-numeric character, please enter a number.")
        number2 = input("\nEnter the second number you'd like to use in the calculation: ")

calculation = input("Enter which calculation you would like to perform: [add, subtract, multiply, divide] ") 
calculation =calculation.lower()                                                                                   #making sure to set anything entered to lower case

if calculation == "add":                                                                  
    calculation = add_func(number1, number2)   

elif calculation == "subtract":
    calculation = subtract_func(number1, number2)

elif calculation == "multiply":
    calculation = multiply_func(number1, number2)

elif calculation == "divide":
    if number2 != 0:                                                                                             #"if" statement to check if "number2" is 0
        calculation = divide_func(number1, number2)                                                              #"number2" is not zero so carrying out the calculation
    else:
        print("\nDivision by zero is not possible please enter a number that is not zero.")                     #new loop for when "number2" is zero that will prompt the user to re-enter a non-zero number
        number2 = input("\nPlease enter a number that is not zero: ")
        while True:                                                                                                        
            if number2.isnumeric() and number2 != "0":
                number2 = float(number2)
                calculation = divide_func(number1, number2)
                break
            else:         
                print("\nThe character you've entered is either non-numeric or 0 please enter a number that is not zero.")
                number2 = input("\nPlease enter a non-zero number: ")

else:
    print("\nThe calculation you've entered is not recognized.")                                                     










   
