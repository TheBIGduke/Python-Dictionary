import json

try:
    # Open the JSON file in read mode
    with open('output.json', 'r') as f:
        # Load the file as a Dictionary
        data =json.load(f)

    # Display the user's information from the loaded data
    print(f"Name: {data['Name']}")
    print(f"Age: {data['Age']}")
    print(f"Height: {data['Height']}m")

# Handle the case where the JSON file doesn't exist
except FileNotFoundError:
    print("Could not find the JSON file")