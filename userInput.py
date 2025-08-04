# This code is to save the user's info in a .JSON file and, then, store them in a Dictionary function to enable communication between two programs

import json 
import time

#Input Validation Functions
def getName():
    while True: # Function that keeps asking the user for the info until received
        name = input("What's your name? >").strip() # Removes any extra spaces from the input
        if name.isalpha(): # Checks the input for letters only
            return name
        print("Please, enter only text")

def getAge():
    while True:
        age = input("How old are you? >").strip()
        if age.isdigit(): # Checks the input for numbers only
            return int(age)
        print("Please, enter only numbers")

def getHeight():
    while True:
        height = input("What's your height? (in m) >").strip()
        try:
            value = float(height)
            return value
        except ValueError:
            pass
        print("Please, enter only numbers")


# Data Collection and Display

name = getName() # Stores the results in variables
age = getAge()
height = getHeight()

print(f"Name : {name}") # Displays formatted output using f-strings
print(f"Age : {age}")
print(f"height : {height}m")


# Dictionary Creation

info = {
    "Name" : name,
    "Age" : age,
    "Height" : height
}


# Get File Name

fileName = input("Enter the file name to save >").strip()
 

# JSON File Operations

try:
    with open(f'{fileName}.json', 'w') as file: # Uses with statement for safe handling and creates a JSON file in write mode with the name specified by the user
        json.dump(info, file, indent=4) # json.dump() converts dictionary to JSON format
    print("\nInformation saved succesfully")
    print("JSON file contents:")
    print(json.dumps(info, indent=4)) # indent=4 creates readable JSON with proper spacing
except Exception as e:
    print(f"Error saving information: {str(e)}")