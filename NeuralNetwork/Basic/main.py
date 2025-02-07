import numpy as np
import nn as nn
import acts


# Input datasets
input_size = 2
# Two hidden layers (len(hidden_layers = 2)) with 2 neurons each
hidden_layers = [2, 2]  
output_size = 1
# Activation functions for each layer
activations = [acts.sigmoid]*3
# Derivatives of activation functions
derivatives = [acts.sigmoid_derivative] * 3  
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_output = np.array([[0], [1], [1], [0]])

# Learning rate
lr = 0.314

# Initialize and train the neural network
SimpleNeuralNetwork = nn.SimpleNeuralNetwork(input_size=input_size, hidden_layers=2, output_size=output_size)
SimpleNeuralNetwork.train(inputs, expected_output, num_epochs=10000, learning_rate=lr)

NeuralNetwork = nn.NeuralNetwork(input_size, hidden_layers, output_size, activations, derivatives)
NeuralNetwork.train(inputs.T, expected_output.T,num_iterations=10000, learning_rate=lr)

# Final prediction after training
print(SimpleNeuralNetwork.predict(inputs).T)
print(NeuralNetwork.predict(inputs.T))
