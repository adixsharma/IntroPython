# Program Name: lab2_car_efficiency.py
# Program Description: The program is a car gas mileage calculator for any(valid) given user inputs of
# tank capacity, MPG, and price per gallon
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
    print("CNET142: {0}".format(name) + "  -  Lab 2: Car Mileage")

    currentTime = datetime.now()
    print (str(currentTime)[0:19])
    print('\n')

# Function name: car_eff
# Function description: the purpose of this function is to calculate cost of driving 100 miles &
# the distance(miles) that one can drive on 1 tank of gas
# @param: None
# @return: returns nothing but prints all calculated data
def car_eff():
    carGasTank = input("Enter the capacity of the car's gas tank (in gallons): ")

    carMpg = input("Enter cars miles per gallon: ")

    gasPrice = input("Enter price per gallon: ")

    cost = (100 / (carMpg)) * gasPrice

    cost = "{:.2f}".format(cost)

    distance = carGasTank * carMpg

    distance = "{:.2f}".format(distance)

    print("Cost of driving 100 miles is $"), cost

    print("Distance on a tank of gas is " + distance + " miles")


if __name__ == '__main__':
    print_me_first('Aditya Sharma')
    car_eff()
