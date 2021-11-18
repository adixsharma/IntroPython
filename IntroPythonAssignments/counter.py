# Program Name: Counter
# Program Description: The purpose of this Program is to open and read a txt file in this case its "test.txt" and the
#   program proceeds to then go line by line and append each line of text in the file to a node in the list. The program
#   then calculates the number of characters in the file excluding some punctuation, number of lines, number of words,
#   number of uppercase characters, number of lowercase characters, number of whitespace, and the number of sentences.
#   It then closes the file and returns all calculated values. Then in the main method we store all returned values in a
#   list(valueList) and then store all nodes in the list to a variable. Once all values have been properly returned and
#   stored in variables we print all lines and values.
# My program performs all the calculations in the function and prints all returned values from the count function in
#   the main.
# This program solves the problem of getting word count and other data points of any txt file.
# @author - Aditya Sharma

# import library to get current time function
from datetime import datetime

fileName = "test.txt"
lineList = list()
valueList = list()

# sys library

# Function name: print_me_first
# Function description: the purpose of this function is to print out my name and lab assignment #
# @param: string "name" is passed as param
# @return: returns nothing but prints name and lab assignment
def print_me_first(name):
    print("CNET142: {0}".format(name) + "  -  Lab 5: File Counter")
    currentTime = datetime.now()
    print ("counter.py")
    print (str(currentTime)[0:19])
    print('\n')

# Function name: count
# Function description: Open and read a txt file in this case "test.txt" is passed as a param and the
#   function then goes line by line and appends each line of text in the file to a node in lineList. The function
#   then calculates the number of characters in the file excluding some punctuation, number of lines, number of words,
#   number of uppercase characters, number of lowercase characters, number of whitespace, and the number of sentences.
#   It then closes the file and returns all calculated values.
# @param: 2 parameters fileName, and lineList
# @return: numOfLines, numOfWords, numOfCharacters, lineList, uppercase_count, lowercase_count, whitespace_count
#         , digit_count, numOfSentences
def count(fileName, lineList):

    txt_file = open(fileName, 'r')

    lines = txt_file.readlines()
    numOfCharacters = 0
    numOfLines = 0
    numOfWords = 0
    tempCounter = 0
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    whitespace_count = 0
    numOfSentences = 0

    for line in lines:
        # print ("Line " + str(lineCount) + ": " + line)
        lineList.append(line)

    for line in lines:
        line = line.strip("\n")
        words = line.split()
        numOfLines += 1
        numOfWords += len(words)
        numOfCharacters += len(line)

    for chars in lines:
        for c in chars:
            if c.isupper():
                uppercase_count += 1
            elif c.islower():
                lowercase_count += 1
            if (' ') in c:
                whitespace_count += 1
            elif c.isdigit():
                digit_count += 1

    for line in lines:
        if (',') in line:
            tempCounter += 1
        if ('\'') in line:
            tempCounter += 1
        if ('.') in line:
            numOfSentences += 1
            tempCounter += 1

    numOfCharacters = numOfCharacters - tempCounter - 1

    txt_file.close()

    return numOfLines, numOfWords, numOfCharacters, lineList, uppercase_count, lowercase_count, whitespace_count\
        , digit_count, numOfSentences

if __name__ == '__main__':

    print_me_first('Aditya Sharma')

    valueList = count(fileName, lineList)

    numOfLines = valueList[0]
    numOfWords = valueList[1]
    numOfCharacters = valueList[2]
    uppercase_count = valueList[4]
    lowercase_count = valueList[5]
    digit_count = valueList[7]
    whitespace_count = valueList[6]
    numOfSentences = valueList[8]
    lineCount = 1

    lineList = valueList[3]

    for sentence in lineList:
        print ("Line " + str(lineCount) + ": " + sentence)
        lineCount += 1
    print ("\n")

    print("Total Number of lines: " + str(numOfLines))
    print("Total Number of words: " + str(numOfWords))
    print("Total Number of characters: " + str(numOfCharacters))
    print ("Total Number of uppercase letters: " + str(uppercase_count))
    print ("Total Number of lowercase letters: " + str(lowercase_count))
    print ("Total Number of spaces: " + str(whitespace_count))
    print ("Total Number of digits: " + str(digit_count))
    print ("Total Number of sentences: " + str(numOfSentences))
