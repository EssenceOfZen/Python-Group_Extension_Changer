# Mass Extension Changer
# Coded by Zane ZenOokami Blalock
# Essence Of Zen

# This program essentially takes in your entered directory and changes any specified extension
# with another extension specified.

# To-Do =========
# *Add Menu
# *Add more user-proofing
# *Create a GUI?


import os

# Global Variables ===========================
VERSION = "1.3.1" # A variable to call for showing update once menu is made

DIRECTORY = "" # used for the directory url location
DIRECTORY_ITEMS = [] # This is an array to house the items inside the directory

# Functions ===========================
def changeDirectory(): # Function allows to change the Directory
    global DIRECTORY

    # We ask for the directory
    directory = "" # Create an empty string for the directory location
    user_input = input("Please enter directory location: ") # Have the user input the directory - they can copy and paste from window's explorer
    for item in user_input: # If the directory uses backslash (like from window's syntax), change them to forward slash for Python's syntax
        if item == '\\':
            item = '/'
        directory += item

    length = len(directory) # We grab the length of the directory, and use -1 to get the index of the last character
    if directory[length-1] != "/": # If there isn't a / at the end of the directory, add one.
        directory += "/"

    DIRECTORY = directory # We set the global variable


def printDirectoryItems(directory): # Prints the items found in the Directory **REDO THIS CODE LATER SINCE UPDATE
    global DIRECTORY_ITEMS
    directory_items = os.listdir(directory) # Sets a variable to be an array of items
    print("Printing Files and Folders: ")
    for item in directory_items:
        print(item)

    DIRECTORY_ITEMS = directory_items

def changeExtension(selection, target):
    global DIRECTORY
    global DIRECTORY_ITEMS


    for file in DIRECTORY_ITEMS:
        current_file = os.path.join(DIRECTORY, file) # We add the folder's url to the file name to create file's url
        if selection in current_file:
            print(current_file)
            new_name = current_file.replace(selection, target)
            output = os.rename(current_file, new_name)

def updateDirectory():
    global DIRECTORY
    global DIRECTORY_ITEMS

    DIRECTORY_ITEMS = os.listdir(DIRECTORY)

# Main Function
def main():
    global DIRECTORY
    global DIRECTORY_ITEMS
    # Start the program by getting the directory
    # Later create a menu

    switch = 1
    while switch == 1:
        changeDirectory()
        # directory_items = os.listdir(DIRECTORY)
        print()

        printDirectoryItems(DIRECTORY)

        print()

        print("Please enter your target extension to change")
        selection = input("please enter extension such as .txt or .html: ")
        print()
        print("Please enter what extension you wanted to switch it to")
        target = input("please enter extension different than before: ")

        print()
        changeExtension(selection, target)
        print()
        updateDirectory()

        answer = input("Are you finished?: ").lower()
        loop = 1
        while loop == 1:
            if answer == "yes" or answer == "y":
                loop = 0
                switch = 0
            elif answer == "no" or answer == "n":
                loop = 0
                switch = 1
            else:
                print("Answer is invalid, try again please.")
                loop = 1

main()