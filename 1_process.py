import json

def extract_full_reviews(entry):
    # Extracting the full content of reviews
    full_reviews = []
    for review in entry.get('reviews', []):
        review_data = {
            'name': review.get('name', ''),
            'text': review.get('text', ''),
            'publishAt': review.get('publishAt', ''),
            'stars': review.get('stars', None),
            # Additional fields can be added here if needed
        }
        full_reviews.append(review_data)

    extracted_entry = {
        'Address': entry.get('address', ''),
        'Category Name': entry.get('categoryName', ''),
        'Cid': entry.get('cid', ''),
        'City': entry.get('city', ''),
        'Latitude': entry.get('location', {}).get('lat', None),
        'Longitude': entry.get('location', {}).get('lng', None),
        'Place ID': entry.get('placeId', ''),
        'Rank': entry.get('rank', ''),
        'Reviews': full_reviews,  # Including full review content
        'Reviews Distribution': entry.get('reviewsDistribution', {}),
        'Street': entry.get('street', ''),
        'Title': entry.get('title', ''),
        'Total Score': entry.get('totalScore', '')
    }
    return extracted_entry

def process_and_save_file(file_name):
    input_path = f'{file_name}.json'
    output_path = f'{file_name}_post.json'
    
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        cleaned_data = [extract_full_reviews(entry) for entry in data]
        
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(cleaned_data, file, ensure_ascii=False, indent=4)
        
        print(f'Processed and saved data to {output_path} successfully.')
        
    except FileNotFoundError:
        print(f'File {input_path} not found.')
    except json.JSONDecodeError:
        print(f'Error decoding JSON from file {input_path}.')

if __name__ == '__main__':
    file_names = ['dc_hotel', 'dc_utils', 'hu_hotel', 'hu_utils', 'la_hotel', 'la_utils', 'ny_hotel', 'ny_utils']
    for file_name in file_names:
        process_and_save_file(file_name)
