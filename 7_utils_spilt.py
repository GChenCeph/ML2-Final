import json
from collections import defaultdict

def load_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data_to_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

utils_data = load_json_data('hu_utils_filtered.json')

category_datasets = defaultdict(list)
for util in utils_data:
    category = util['Category Name'].replace(' ', '_').replace('/', '_').lower()
    category_datasets[category].append(util)

for category, data in category_datasets.items():
    filename = f'hu_{category}_utils.json'
    save_data_to_json(data, filename)

print(f"Generated files: {list(category_datasets.keys())}")
