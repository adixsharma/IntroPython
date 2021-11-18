# This program prints out my name and course as well as the current timestamp
# The purpose of the program is to get familiar with our local IDE, create and run a .py file, and print w/ formatting
# @param - name
# @return - msg
# @author - Aditya Sharma


# import library to get current time function
from datetime import datetime

# sys library

def print_me_first(name):
    # print('\n')
    # print("CNET142: {0}".format(name))
    #
    # currentTime = datetime.now()
    # print (str(currentTime)[0:19])

    print('\n')
    msg = "\n" + "{:12}".format("Name") + ": " + name + "\n"
    msg = msg + "{:12}".format("Program") + ": " + "usa_Olympics.py" + "\n"

    currentTime = datetime.now()
    msg = msg + "{:12}".format("Current Time") + ": " + str(currentTime)[0:19]
    print('\n')

    return msg


if __name__ == '__main__':
    print_me_first('Aditya Sharma')