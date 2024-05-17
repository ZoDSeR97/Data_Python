import numpy as np
import acts

epsilon = 1e-10  # Small epsilon value to avoid division by zero

# 1 Layer NN
class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_layers, output_size, activation=acts.sigmoid, derivative=acts.sigmoid_derivative):
        self.input_size = input_size
        self.hidden_layers = hidden_layers
        self.output_size = output_size
        self.activation = activation
        self.derivative = derivative

        # Initialize weights and biases
        self.hidden_weights = np.random.uniform(size=(input_size, hidden_layers))
        self.hidden_bias = np.random.uniform(size=(1, hidden_layers))
        self.output_weights = np.random.uniform(size=(hidden_layers, output_size))
        self.output_bias = np.random.uniform(size=(1, output_size))
    
    def forward_propagation(self, inputs):
        hidden_layer_activation = np.dot(inputs, self.hidden_weights)
        hidden_layer_activation += self.hidden_bias
        hidden_layer_output = self.activation(hidden_layer_activation)

        output_layer_activation = np.dot(
            hidden_layer_output, self.output_weights)
        output_layer_activation += self.output_bias
        predicted_output = self.activation(output_layer_activation)

        return predicted_output, hidden_layer_output

    def backward_propagation(self, inputs, predicted_output, hidden_layer_output, expected_output, learning_rate):
        error = expected_output - predicted_output
        d_predicted_output = error * self.derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(self.output_weights.T)
        d_hidden_layer = error_hidden_layer * self.derivative(hidden_layer_output)

        # Update weights and biases
        self.output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
        self.output_bias += np.sum(d_predicted_output,axis=0, keepdims=True) * learning_rate
        self.hidden_weights += inputs.T.dot(d_hidden_layer) * learning_rate
        self.hidden_bias += np.sum(d_hidden_layer,axis=0, keepdims=True) * learning_rate

    def train(self, inputs, expected_output, num_epochs, learning_rate):
        for epoch in range(num_epochs):
            predicted_output, hidden_layer_output = self.forward_propagation(inputs)
            self.backward_propagation(inputs, predicted_output, hidden_layer_output, expected_output, learning_rate)

    def predict(self, inputs):
        predicted_output, _ = self.forward_propagation(inputs)
        predictions = (predicted_output > 0.5).astype(int)
        return predictions

# X Layers NN (Work in progress)
class NeuralNetwork:
    def __init__(self, input_size, hidden_layers, output_size, activations: list, derivatives: list):
        self.input_size = input_size
        self.hidden_layers = hidden_layers
        self.output_size = output_size
        self.activations = activations
        self.derivatives = derivatives
        self.parameters = {}
        self.gradients = {}

        # Initialize weights and biases
        layer_sizes = [input_size] + hidden_layers + [output_size]
        for i in range(1, len(layer_sizes)):
            self.parameters[f"W{i}"] = np.random.randn(layer_sizes[i], layer_sizes[i-1]) * 0.01
            self.parameters[f"b{i}"] = np.zeros((layer_sizes[i], 1))

    def forward_propagation(self, X):
        cache = {"A0": X}

        for l in range(1, len(self.parameters)//2 + 1):
            Z = np.dot(self.parameters[f"W{l}"], cache[f"A{l-1}"]) + self.parameters[f"b{l}"]
            A = self.activations[l-1](Z)
            cache[f"Z{l}"] = Z
            cache[f"A{l}"] = A

        return cache[f"A{len(self.parameters)//2}"], cache

    def backward_propagation(self, X, Y, cache):
        m = X.shape[1]
        dA_prev = -(np.divide(Y, cache[f"A{len(self.parameters)//2}"] + epsilon) - np.divide(1 - Y, 1 - cache[f"A{len(self.parameters)//2}"] + epsilon))

        for l in reversed(range(1, len(self.parameters)//2 + 1)):
            dZ = dA_prev * self.derivatives[l-1](cache[f"Z{l}"])
            self.gradients[f"dW{l}"] = (1/m) * np.dot(dZ, cache[f"A{l-1}"].T)
            self.gradients[f"db{l}"] = (1/m) * np.sum(dZ, axis=1, keepdims=True)
            dA_prev = np.dot(self.parameters[f"W{l}"].T, dZ)

    def update_parameters(self, learning_rate):
        for l in range(1, len(self.parameters)//2 + 1):
            self.parameters[f"W{l}"] -= learning_rate * self.gradients[f"dW{l}"]
            self.parameters[f"b{l}"] -= learning_rate * self.gradients[f"db{l}"]

    def train(self, X, Y, num_iterations, learning_rate):
        for i in range(num_iterations):
            AL, cache = self.forward_propagation(X)
            cost = -np.mean(Y * np.log(AL + epsilon) + (1 - Y) * np.log(1 - AL + epsilon))
            self.backward_propagation(X, Y, cache)
            self.update_parameters(learning_rate)
            """ 
            if i % 100 == 0:
                print(f"Iteration {i}, Cost: {cost}")
            """
    def predict(self, X):
        AL, _ = self.forward_propagation(X)
        predictions = (AL > 0.5).astype(int)
        return predictions
