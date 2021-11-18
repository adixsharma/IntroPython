# Program Name: MenuFunction
# Program Description:
# @author - Aditya Sharma


# import library to get current time function
from datetime import datetime
from interestCalculator import interestCalc

# sys library

# Function name: print_me_first
# Function description: the purpose of this function is to print out my name and lab assignment #
# @param: string "name" is passed as param
# @return: returns nothing but prints name and lab assignment
def print_me_first(name):
    print('\n')
    print("CNET142: {0}".format(name) + "  -  Lab 4: Menu Function")
    currentTime = datetime.now()
    print (str(currentTime)[0:19])

# Function name: mortgagePayment
# Function description: the purpose of this function is to calculate the monthly mortgage payment
# @param: string "name" is passed as param
# @return: returns nothing but prints name and lab assignment
def mortgagePayment():
    # random value assignment to enter while loop
    loan_amt = 1

    while loan_amt > 0:

        loan_amt = input("Enter the Loan Amount, 0 to quit: ")

        if loan_amt == 0:
            print("Exiting Mortgage Payment Calculator.....")
            break

        interestRate = input("Enter the Loan interest rate % : ")
        monthlyRate = (interestRate/100)/12

        term = input("Enter the Loan term (number of years): ")
        months = term*12

        # M = L(I(1 + I)**N) / ((1 + I)**N - 1)
        monthlyPayment = (loan_amt * (monthlyRate * (1 + monthlyRate) ** months)) / (((1 + monthlyRate) ** months) - 1)

        totalPayment = monthlyPayment * months

        totalInterest = totalPayment - loan_amt

        totalInterest = "{:.2f}".format(totalInterest)
        totalPayment = "{:.2f}".format(totalPayment)
        monthlyPayment = "{:.2f}".format(monthlyPayment)
        loan_amt = "{:.2f}".format(loan_amt)

        print("For the Loan Amount of $" + str(loan_amt) + " for " + str(term) + " years with an interest rate of " +
              str(interestRate) + "%")

        print("The monthly payment is $" + monthlyPayment)

        print ("The total amount paid for this loan is $" + totalPayment)
        print ("Total interest paid for this loan is $" + totalInterest)

def menu(userIn):

    userIn = input("""
        --------------------------------
        1:  Calculate Simple Interest
        2:  Calculate Mortgage Payment
        99: Quit Program
        --------------------------------
        
        Select One of the commands above:  """)

    if userIn == 1:
        interestCalc()
    elif userIn == 2:
        mortgagePayment()
    elif userIn == 99:
        print("\n    Have a nice day !")
        exit()
    else:
        print("Error: Command not recognized")
        menu()

if __name__ == '__main__':

    true = 3

    print (true)
    print_me_first('Aditya Sharma')

    switch = 0

    while switch != 99:
        menu(switch)
