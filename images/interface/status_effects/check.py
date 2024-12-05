import os
import re

# Path to your JavaScript file
file_path = "E:/tweego/src/secretary/source/js/tmpeffect_static.js"  # Replace this with the actual path

# Directory where the image files are located (same as the JS file's directory)
directory = os.getcwd()

# Regex to match keys in tmpEffectsStatic (assuming standard JS object notation)
key_pattern = re.compile(r'tmpEffectsStatic\["(\w+)"\]')

# ANSI color codes for terminal output
GREEN = '\033[92m'  # Bright Green
RED = '\033[91m'    # Bright Red
RESET = '\033[0m'   # Reset to default color

# Read the JavaScript file
with open(file_path, 'r', encoding='utf-8') as file:
    js_content = file.read()

# Extract keys from the file content
keys = key_pattern.findall(js_content)

# Prepare list to hold results
results = []

# Check each key for a corresponding .png file in the directory
for key in keys:
    image_file = f"{key}.png"
    image_path = os.path.join(directory, image_file)
    print(image_path)
    if os.path.isfile(image_file):
        results.append({"key": key, "file_found": True})
    else:
        results.append({"key": key, "file_found": False})

# Print the results with colors
for result in results:
    status = "Found" if result["file_found"] else "Not Found"
    color = GREEN if result["file_found"] else RED
    print(f"{color}{result['key']}: {status}{RESET}")