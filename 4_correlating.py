import json
import pandas as pd
from scipy.stats import pearsonr

# Helper function to load JSON data
def load_json_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Load the distance matrix from a CSV file, excluding the first column (hotel identifiers)
def load_csv_to_matrix(filename):
    df = pd.read_csv(filename)
    return df.iloc[:, 1:].values.tolist()  # Exclude the first column (hotel identifiers)

# Count the number of utilities within a specified radius for each hotel
def count_utilities_within_radius(dist_matrix, threshold):
    return [sum(dist <= threshold for dist in row) for row in dist_matrix]

# List of city prefixes
city_prefixes = ['hu']


# Process each city's data
for city_prefix in city_prefixes:
    hotels_data = load_json_data(f'{city_prefix}_hotel_filtered.json')
    distance_matrix = load_csv_to_matrix(f'{city_prefix}_distance_matrix.csv')

    # Define a distance threshold in kilometers (e.g., 5 km)
    distance_threshold = 1.0

    # Calculate the count of utilities within the threshold distance
    # i want to calculate here with a loop each of the different util types or categories and then make an array list
    # or maybe some sort of key pair data structure then we can use that to calculate each categories
    # pearson correlation coefficient info
    utilities_count_within_radius = count_utilities_within_radius(distance_matrix, distance_threshold)

    # Extract the total scores from the hotel data
    total_scores = [hotel.get('Total Score', 0) for hotel in hotels_data]
    revenue = [hotel.get('Total Room Receipts', 0) for hotel in hotels_data]

    # Calculate the Pearson correlation coefficient between counts and total scores
    correlation, p_value = pearsonr(utilities_count_within_radius, total_scores)
    correlation_rev, rev_p_value = pearsonr(utilities_count_within_radius, revenue)
    correlation_rate, rate_p_value = pearsonr(total_scores, revenue)
    print(f'{city_prefix.upper()}: Pearson Correlation Coefficient = {correlation}')
    print(f'p-value = {p_value}')
    print(f'{city_prefix.upper()}: Pearson Correlation Coefficient = {correlation_rev}')
    print(f'p-value = {rev_p_value}')
    print(f'{city_prefix.upper()}: Pearson Correlation Coefficient = {correlation_rate}')
    print(f'p-value = {rate_p_value}')

