# Load Python's built-in JSON and folder-path tools
import json
from pathlib import Path

# Function (like a Nuke Gizmo) that reads one JSON file and prints a clean shot report
def summarize_shot_file(file_path):
    # Open and load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)

    # Check if the JSON file holds a list of shots (like shots_batch.json)
    if isinstance(data, list):
        print(f"\n--- Batch File: {file_path.name} ({len(data)} shots) ---")
        for shot in data:
            print(f"  Shot: {shot['name']} | FPS: {shot['fps']} | Frames: {shot['frames']} | Priority: {shot['priority']}")
        return len(data)

    # Otherwise, it holds a single shot dictionary (like shots.json)
    else:
        print(f"\n--- Single Shot File: {file_path.name} ---")
        print(f"  Shot: {data['name']} | FPS: {data['fps']} | Artist: {data['artist']}")
        return 1

# Main function that scans a folder for all .json files and totals the shots
def run_pipeline_report(folder_path):
    folder = Path(folder_path)
    total_shots = 0

    # Loop through every .json file in the folder
    for json_file in folder.glob("*.json"):
        total_shots = total_shots + summarize_shot_file(json_file)

    print(f"\nPipeline Summary Complete: {total_shots} total shot entries found.")
    return total_shots

# Run the report on the current folder (".")
run_pipeline_report(".")