from torch.utils.data import Dataset, DataLoader
import torch

class CustomDataloader(Dataset):
    def __init__(self, matrix, scores, correlations, revenue):
        self.matrix = matrix
        self.scores = scores
        self.correlations = correlations  # This should include both Pearson coefficients and p-values
        self.revenue = revenue

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, idx):
        # Extracting both Pearson coefficients and p-values for each correlation data point
        correlation_features = [value for key, values in self.correlations.items() for value in values.values()]
        print(idx)
        
        # Constructing the full feature vector
        features = self.matrix[idx] + [self.scores[idx]] + correlation_features
        target = self.revenue[idx]

        return torch.tensor(features, dtype=torch.float32), torch.tensor(target, dtype=torch.float32)
