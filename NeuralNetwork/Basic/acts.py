import numpy as np

# Sigmoid activation function and its derivative

def sigmoid(x):
    return np.where(x >= 0, 1 / (1 + np.exp(-x)), np.exp(x) / (1 + np.exp(x)))

def sigmoid_derivative(x):
    return x * (1 - x)

# ReLU (Rectified Linear Unit) activation function and its derivative

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Hyperbolic tangent (tanh) activation function and its derivative
def tanh(x):
    return np.tanh(x)


def tanh_derivative(x):
    return 1 - x**2

# Softmax activation function
def softmax(x):
    exp_vals = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_vals / np.sum(exp_vals, axis=-1, keepdims=True)
