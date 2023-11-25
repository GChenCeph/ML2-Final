# model.py
import torch.nn as nn
import torch.nn.functional as F

class RegressionNN(nn.Module):
    def __init__(self, input_size):
        super(RegressionNN, self).__init__()
        # Define the layers of the neural network
        self.fc1 = nn.Linear(input_size, 64)  # Input layer
        self.fc2 = nn.Linear(64, 32)  # Hidden layer
        self.fc3 = nn.Linear(32, 1)   # Output layer

    def forward(self, x):
        # Define forward pass through the network
        x = F.leaky_relu(self.fc1(x), negative_slope=0.01)
        x = F.leaky_relu(self.fc2(x), negative_slope=0.01)
        x = self.fc3(x)  # No activation function for the output layer in regression
        return x
