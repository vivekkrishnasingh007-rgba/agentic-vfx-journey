# Load Python's built-in JSON tool and modern folder-path tool
import json
from pathlib import Path

# Define a reusable function (like a Nuke Gizmo) that scans a folder for JSON files
def scan_json_files(folder_path):
    # Turn the text path into a Path object Python can search
    folder = Path(folder_path)
    # Keep count of how many JSON files we find
    json_count = 0

    # Loop through every file in the folder that ends with ".json"
    for json_file in folder.glob("*.json"):
        # Open and read the JSON file
        with open(json_file, "r") as file:
            data = json.load(file)

        # Print the file name and what is inside it
        print("Found:", json_file.name, "| Content:", data)
        # Add 1 to our counter
        json_count = json_count + 1

    # Send the final count back out of the function
    return json_count

# Call the function on the current folder (".") and save the returned count
total = scan_json_files(".")
print("Total JSON files scanned:", total)