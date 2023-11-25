import json
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from model import RegressionNN
from torch.utils.data import DataLoader
import cloader as loader


####################################################
def load_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data_to_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def load_csv_to_matrix(filename):
    df = pd.read_csv(filename)
    return df.iloc[:, 1:].values.tolist()
####################################################


def main():
    
    # Parameters
    input_size = 1000
    batch_size = 32
    alpha = 0.001
    num_epochs = 100

    # Load data
    correlation = load_json_data('category_correlations.json')
    matrix = load_csv_to_matrix('hu_distance_matrix.json')
    hotels = load_json_data('hu_hotel_filtered.json')
    scores = [hotel.get('Total Score', 0) for hotel in hotels]
    revenue = []  # Placeholder

    dataset = loader(matrix, scores, correlation, revenue)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Model
    model = RegressionNN(input_size)

    # Loss and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=alpha)

    # Training loop
    for epoch in range(num_epochs):
        for i, (features, targets) in enumerate(data_loader):
            # Forward pass
            outputs = model(features)
            loss = criterion(outputs, targets)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i + 1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(data_loader)}], Loss: {loss.item():.4f}')

    # Save the model
    torch.save(model.state_dict(), 'model.pth')

if __name__ == "__main__":
    main()