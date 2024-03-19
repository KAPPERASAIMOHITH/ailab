import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def initialize_parameters(input_size, hidden_size, output_size):
    return np.random.rand(input_size, hidden_size), np.zeros((1, hidden_size)), np.random.rand(hidden_size, output_size), np.zeros((1, output_size))

def forward(X, weights_input_hidden, bias_hidden, weights_hidden_output, bias_output):
    hidden_layer_output = sigmoid(np.dot(X, weights_input_hidden) + bias_hidden)
    predicted_output = sigmoid(np.dot(hidden_layer_output, weights_hidden_output) + bias_output)
    return predicted_output


input_size, hidden_size, output_size = 3, 4, 1
weights_input_hidden, bias_hidden, weights_hidden_output, bias_output = initialize_parameters(input_size, hidden_size, output_size)
input_data = np.array([[0.2, 0.3, 0.4]])
predicted_output = forward(input_data, weights_input_hidden, bias_hidden, weights_hidden_output, bias_output)
print("Predicted Output:", predicted_output)
