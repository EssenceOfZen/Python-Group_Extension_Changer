# Mass Extension Changer
# Coded by Zane ZenOokami Blalock
# http://EssenceOfZen.org/

# This program essentially takes in your entered directory and changes any specified extension
# with another extension specified.

# Feel free to fork this project and make what you will with it, we simply ask that you give credit, and link back
# to our source location at our site (EssenceOfZen.org) and our GitHub. Thank you <3

# TODO: Add Menu
# TODO: Add more user-proofing
# TODO: Create a GUI?
# TODO: Create more console communication to know what's going on


import os
from tkinter import filedialog
import EssencePython
from tkinter import *

# Global Variables ===========================
VERSION = "1.9.00" # A variable to call for showing update once menu is made

DIRECTORY = "" # used for the directory url location
DIRECTORY_ITEMS = [] # This is an array to house the items inside the directory
ROOT = Tk()

# Functions ===========================
def changeDirectory(): # Function allows to change the Directory
    global DIRECTORY

    # We ask for the directory
    directory = "" # Create an empty string for the directory location
    print("(You can copy the url from window's explorer directory bar)")
    user_input = input("Please enter directory location: ") # Have the user input the directory - they can copy and paste from window's explorer
    for item in user_input: # If the directory uses backslash (like from window's syntax), change them to forward slash for Python's syntax
        if item == '\\':
            item = '/'
        directory += item

    length = len(directory) # We grab the length of the directory, and use -1 to get the index of the last character
    if directory[length-1] != "/": # If there isn't a / at the end of the directory, add one.
        directory += "/"
        print("Added '/' to the url!")
        print("")

    DIRECTORY = directory # We set the global variable
    print("Directory Changed!")
    print("")


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
        else:
            print("Selection was not found...")
            print("")

def updateDirectory(): # Updates the Directory with any changes that you've made on the files.
    global DIRECTORY
    global DIRECTORY_ITEMS

    DIRECTORY_ITEMS = os.listdir(DIRECTORY)

def directoryDialog(root):
    root.fileDirectory = filedialog.askdirectory()
    return root.fileDirectory


def menu(): # TODO: Finish this function
    pass

# Tkinter functions ================================================================================================
def initializeGUI():
    pass


# Main Function ====================================================================================================
def main():
    EssencePython.EoZ_Logo() # Calls our Console logo

    # Pull down our global variables for the main function
    global DIRECTORY
    global DIRECTORY_ITEMS
    global ROOT
    # Start the program by getting the directory
    # Later create a menu

    main_switch = 1
    while main_switch == 1:
        changeDirectory() # Deprecated
        #DIRECTORY = directoryDialog(ROOT)
        #print(DIRECTORY)

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
        continue_loop = 1
        while continue_loop == 1:
            if answer == "yes" or answer == "y":
                continue_loop = 0
                main_switch = 0
            elif answer == "no" or answer == "n":
                continue_loop = 0
                main_switch = 1
            else:
                print("Answer is invalid, try again please.")
                continue_loop = 1

main()