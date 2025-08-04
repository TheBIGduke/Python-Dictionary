# This code is to save the user's info in a .JSON file and, then, store them in a Dictionary function to enable communication between two programs
import json 

def getName():
    while True:
        name = input("What's your name? >").strip()
        if name.isalpha():
            return name
        print("Please, enter only text")

def getAge():
    while True:
        age = input("How old are you? >").strip()
        if age.isdigit():
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

name = getName()
age = getAge()
height = getHeight()

print(f"Name : {name}")
print(f"Age : {age}")
print(f"height : {height}m")


info = {
    "Name" : name,
    "Age" : age,
    "height" : height
}
    
try:
    with open('output.json', 'w') as file:
        json.dump(info, file, indent=4)
    print("\nInformation saved succesfully")
    print("JSON file contents:")
    print(json.dumps(info, indent=4))
except Exception as e:
    print(f"Error saving information: {str(e)}")