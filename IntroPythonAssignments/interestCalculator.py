# Program Name: interestCalculator
# Program Description: The program is a Interest rate calculator for any(valid) given user input
# @author - Aditya Sharma


# import library to get current time function
from datetime import datetime

# sys library

# Function name: print_me_first
# Function description: the purpose of this function is to print out my name and lab assignment #
# @param: string "name" is passed as param
# @return: returns nothing but prints name and lab assignment
def print_me_first(name):
    print('\n')
    print("CNET142: {0}".format(name) + "  -  Lab 3: Interest Rate")

    currentTime = datetime.now()
    print (str(currentTime)[0:19])
    print('\n')

# ORIGINAL PROGRAM
# Function name: interestCalc

# Function description: The purpose of this function is to take user inputted interest rate data
# and calculates the interest earned and total after said num of years

# @param: no parameters passed
# @return: returns nothing but prints interest rate information calculated
# def interstCalc():
#     # random value assignment to enter while loop
#     p = 1
#
#     while p > 0:
#
#         p = input("Enter the starting principle, 0 to quit: ")
#
#         if p <= 0:
#             print("Program exiting.....")
#             break
#
#         r = input("Enter the annual interest rate: ")
#         n = input("How many times per year is the account compounded? ")
#         t = input("For how many years will the account earn interest? ")
#
#         total = p * ((1 + float(r / 100) / n) ** (n * t))
#         interest = total - p
#
#         total = "{:.2f}".format(total)
#         interest = "{:.2f}".format(interest)
#
#        print("At the end of " + str(t) + " year(s) you will have $" + str(total) + " with an interest earned $" + str(
#             interest))
#         print('\n')

# Function name: interestCalc

# Function description: The purpose of this function is to take user inputted interest rate data
# and calculates the interest earned and total after said num of years

# @param: no parameters passed
# @return: returns nothing but prints interest rate information calculated
def interestCalc():
    # random value assignment to enter while loop
    p = 1

    while p > 0:

        print("\n\nCalculating Simple Interest")

        p = input("\nEnter the starting principle, <= 0 to quit:                                                      ")

        if p <= 0:
            print("Exiting Interest Calculator.....\n\n")
            break

        r = input("Enter the annual interest rate: ")
        n = input("How many times per year is the account compounded? ")
        t = input("For how many years will the account earn interest? ")

        total = p * ((1 + float(r / 100) / n) ** (n * t))
        interest = total - p

        total = "{:.2f}".format(total)
        interest = "{:.2f}".format(interest)

        print("At the end of " + str(t) + " year(s) you will have $" + str(total) + " with an interest earned $" + str(
            interest))


if __name__ == '__main__':
    print_me_first('Aditya Sharma')
    interestCalc()

