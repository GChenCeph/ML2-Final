from torch.utils.data import Dataset, DataLoader
import torch

class CustomDataloader(Dataset):
    def __init__(self, matrix, scores, correlations, revenue):
        self.matrix = matrix
        self.scores = scores
        self.correlations = correlations
        self.revenue = revenue

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, idx):
        features = self.matrix[idx] + [self.scores[idx]] + self.correlations[idx]
        target = self.revenue[idx]

        return torch.tensor(features, dtype=torch.float32), torch.tensor(target, dtype=torch.float32)
