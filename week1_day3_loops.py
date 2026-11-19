# Load Python's built-in JSON tool
import json

# A list of shot dictionaries (each item is one shot)
shots = [
    {"name": "SH010", "fps": 24, "frames": 80},
    {"name": "SH020", "fps": 25, "frames": 150},
    {"name": "SH030", "fps": 24, "frames": 95},
    {"name": "SH040", "fps": 24, "frames": 200}
]

# Empty list to store our tagged results
processed_shots = []

# Loop through every shot one by one
for shot in shots:
    # Check if the shot is longer than 100 frames (like a Nuke Switch node)
    if shot["frames"] > 100:
        shot["priority"] = "Heavy"
    else:
        shot["priority"] = "Standard"

    # Print the result for this shot
    print(shot["name"], "->", shot["frames"], "frames ->", shot["priority"])
    # Add the updated shot to our processed list
    processed_shots.append(shot)

# Save the full batch list to a new JSON file
with open("shots_batch.json", "w") as file:
    json.dump(processed_shots, file, indent=4)

print("Saved batch to shots_batch.json!")
