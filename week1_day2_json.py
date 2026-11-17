# Load Python's built-in tool for reading and writing JSON files
import json

# Create a dictionary describing one VFX shot (like a node's knobs)
shot = {
    "name": "SH010",
    "fps": 24,
    "frame_range": [1001, 1120],
    "artist": "Vivek",
}

# Open (or create) "shots.json" in write mode ("w") and save the dictionary inside
with open("shots.json", "w") as file:
    json.dump(shot, file, indent=4)  # indent=4 formats it neatly on multiple lines

print("Saved shot to shots.json!")

# Open "shots.json" in read mode ("r") and load the data back into Python
with open("shots.json", "r") as file:
    loaded_shot = json.load(file)

# Print values from the loaded dictionary to prove it read back cleanly
print("Read back from file ->", loaded_shot)
print("Artist:", loaded_shot["artist"])
print("Frame range:", loaded_shot["frame_range"])