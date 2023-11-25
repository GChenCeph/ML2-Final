import json
import spacy
from textblob import TextBlob

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Function to load JSON data
def load_json_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to save data to a JSON file
def save_data_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

# Analyze reviews
def analyze_review(review):
    text = review.get('text', '')
    if text:
        # Sentiment analysis
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity

        # NER to identify utilities
        doc = nlp(text)
        utilities = []
        for ent in doc.ents:
            if ent.label_ in ["GPE", "FAC", "ORG"]:  # Adjust as needed
                utilities.append((ent.text, sentiment_score))

        return sentiment_score, utilities
    return None, None

# Process hotel data
def process_hotel_data(hotels_data):
    for hotel in hotels_data:
        review_sentiments = []
        utility_mentions = {}

        for review in hotel.get('reviews', []):
            sentiment, utilities = analyze_review(review)
            if sentiment is not None:
                review_sentiments.append(sentiment)

            for util, score in utilities:
                utility_mentions.setdefault(util, []).append(score)

        # Debugging: Print out what's being captured
        #print(f"Hotel: {hotel.get('Title')}, Avg Sentiment: {sum(review_sentiments) / len(review_sentiments) if review_sentiments else 0}, Utilities: {utility_mentions}")

        # Aggregate results
        hotel['average_sentiment'] = sum(review_sentiments) / len(review_sentiments) if review_sentiments else 0
        hotel['utility_sentiments'] = {util: sum(scores)/len(scores) for util, scores in utility_mentions.items()}
    
    return hotels_data

hotel_data = load_json_data('hu_hotel_filtered.json')

processed_data = process_hotel_data(hotel_data)

save_data_to_json(processed_data, 'hu_hotel_review_processed.json')
