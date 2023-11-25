import json
from collections import defaultdict

# Function to load JSON data from a file
def load_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to save data to a JSON file
def save_data_to_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Load the utilities data
utils_data = load_json_data('hu_utils_filtered.json')

# Split the utils dataset based on "Category Name" and group them
grouped_utils = defaultdict(list)
for util in utils_data:
    category = util['Category Name'].strip().replace(' ', '_').replace('/', '_').lower()
    grouped_utils[category].append(util)

# Convert defaultdict to a regular dict for JSON serialization
grouped_utils_dict = dict(grouped_utils)

# Save the grouped utils into one JSON file, categorically organized
save_data_to_json(grouped_utils_dict, 'hu_utils_grouped.json')
