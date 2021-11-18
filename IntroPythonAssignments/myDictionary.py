# Program Name: myDictionary.py
# Program Description: The purpose of this program is to create an address book of contacts stored in a dictionary. Then
# a .json file is created and the dictionary contents are appended to it. Next the program reads from the .json file and
# then we perform a search for "Ron" and "Sha" to see if they are in the json file and return the results of
# each the search
# @author - Aditya Sharma

from datetime import datetime
import json


# Function name: print_me_first
# Function description: the purpose of this function is to print out my name and lab assignment #
# @param: string "name" is passed as param
# @return: returns nothing but prints name and lab assignment
def print_me_first(name):
    print('\n')
    print("CNET142     : {0}".format(name) + "  -  Lab 6: Dictionary")
    print("Program     : myDictionary.py")

    currentTime = datetime.now()
    print("Current Time: " + str(currentTime)[0:19])
    print('\n')

# Function name: create_my_contact()
# Function description: the purpose of this function is create and populate a dictionary called my_contacts and
# then return it
# @param: None
# @return: my_contact of type dictionary
def create_my_contact():
    my_contact = {
        01: {"Fname": "John", "Lname": "Smith", "DOB": "1/20/1991",
             "PhoneNum": {"number": "510-600-5400", "Type": "cell"}, "Address": {"Street": "100 main street",
                                                                                 "City": "Fremont", "State": "CA",
                                                                                 "Zipcode": "94536"}},
        02: {"Fname": "Ron", "Lname": "Robertson", "DOB": "5/23/1991", "PhoneNum": {"number": "510-600-8800",
                                                                                    "Type": "cell"},
             "Address": {"Street": "4600 Ohlone Way", "City": "Fremont", "State": "CA",
                         "Zipcode": "94539"}},
        03: {"Fname": "Paul", "Lname": "Washington", "DOB": "6/15/1995", "PhoneNum": {"number": "510-688-1241",
                                                                                      "Type": "cell"},
             "Address": {"Street": "8543 Ohlone Plaza", "City": "Fremont", "State": "CA",
                         "Zipcode": "94539"}}
    }
    return my_contact

# Function name: save_json_file()
# Function description: the purpose of this function is to create a new .json file and append the dictionary
# contact_list to it and indent properly
# @param: fileName of type string and contact_List of type dictionary
# @return: returns nothing
def save_json_file(fileName, contact_List):
    with open(fileName, 'w') as input:
        json.dump(contact_List, input, indent=4)

# Function name: open_json_file()
# Function description: the purpose of this function is to open the .json file and load all the data from it and store
# it to json_data and return it
# @param: string "fileName" is passed
# @return: returns json_data
def open_json_file(fileName):
    with open(fileName, 'r') as out:
        json_data = json.load(out)

    return json_data

# Function name: find_my_contact_key()
# Function description: the purpose of this function is to search through the data returned from reading the json file
# and checking if Fname matched the searchKey passed, it then either prints out all the information of the desired
# searchKey or prints Not Found
# @param: searchFor of type string which is the desired search string to find, and contactList of type Dictionary
# @return: returns nothing
def find_my_contact_key(searchFor, contactList):
    print("Searching for " + searchFor)
    val = False
    for i in contactList.keys():
        for j in contactList[i].keys():
            if contactList[i]["Fname"] == searchFor:
                val = contactList[i]

    if val:
        print("*** " + searchFor + " Found ***\n")

        fName = val["Fname"]
        LName = val["Lname"]
        fullName = fName + " " + LName
        bDay = val["DOB"]
        type = val["PhoneNum"]["Type"]
        num = val["PhoneNum"]["number"]
        street = val["Address"]["Street"]
        city = val["Address"]["City"]
        state = val["Address"]["State"]
        zip = val["Address"]["Zipcode"]

        print("Name: " + fullName)
        print("Birthday: " + bDay)
        print(type + ": " + num)
        print("Address: " + street + "\n         " + city + ", " + state + " " + zip)
        print("\n")
    else:
        print ("***  " + searchFor + " Not Found  ***")


if __name__ == '__main__':
    print_me_first('Aditya Sharma')

    contact_list = create_my_contact()  # create dictionary

    save_json_file("my_contact.json", contact_list)  # save disctionary to JSON file

    json_data = open_json_file('my_contact.json')  # open JSON file load to distionary
    print ("***BEGINNING OF JSON List:\n")
    print(contact_list[01])
    print(contact_list[02])
    print(contact_list[03])
    print("\n***END OF JSON LIST\n\n")

    find_my_contact_key("Ron", json_data)
    find_my_contact_key("Sha", json_data)
