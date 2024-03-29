import numpy as np
import random
import matplotlib.pyplot as plt

COLOUR_NAMES = ["red","orange","yellow","green","blue","purple","black","white"]

def colour_name_to_expected_arr(name):
    if name not in COLOUR_NAMES:
        while True:
            print(name)
    return np.array([int(name == n) for n in COLOUR_NAMES])

def arr_to_colour_name(arr):
    return COLOUR_NAMES[np.argmax(arr)]

def sigmoid(x):
    return 1/(1+np.exp(-x))

def import_weights(weights_filename):
    data = np.load(weights_filename)
    hl_weights = data['hl_weights']
    ol_weights = data['ol_weights']

    return hl_weights, ol_weights

def forward_pass(input_vals, hl_weights, ol_weights):
    # calculating hidden layer outputs
    hidden_nets = np.dot(hl_weights, input_vals)
    hidden_outputs = sigmoid(hidden_nets)
    
    # calculating output layer outputs
    output_nets = np.dot(ol_weights, hidden_outputs)
    output_outputs = sigmoid(output_nets)

    return output_outputs

if __name__ == "__main__":
    INPUT_NEURONS = 3
    HIDDEN_NEURONS = 10
    OUTPUT_NEURONS = 8
    TRAINING_FILE_NAME = "colours_combined.txt"
    EPOCHS = 20
    TRAIN = True

    LEARNING_RATE = 0.5

    training_iterations = 0
    errors = []

    if TRAIN:
        hl_weights = np.random.rand(HIDDEN_NEURONS, INPUT_NEURONS) # rows, columns
        ol_weights = np.random.rand(OUTPUT_NEURONS, HIDDEN_NEURONS)

        with open(TRAINING_FILE_NAME, "r") as f:
            training_data = f.readlines()
            random.shuffle(training_data) # randomizes the order of the training data

            for epoch in range(0, EPOCHS):
                for t in training_data:
                    data = t.split()

                    # FORWARD PASS
                    input_vals = np.array([float(data[i]) for i in range(0, INPUT_NEURONS)])

                    # calculating hidden layer outputs
                    hidden_nets = np.dot(hl_weights, input_vals)
                    hidden_outputs = sigmoid(hidden_nets)
                    
                    # calculating output layer outputs
                    output_nets = np.dot(ol_weights, hidden_outputs)
                    output_outputs = sigmoid(output_nets)

                    # calculating error
                    error = np.sum(0.5*(colour_name_to_expected_arr(data[3]) - output_outputs)**2)
                    print(f"Error: {error}\nTraining iterations: {training_iterations}")
                    errors.append(error)
                    training_iterations += 1
                    
                    # BACKWARD PASS

                    # calculating the changes on the output layer weights
                    d_error_d_outs = -(colour_name_to_expected_arr(data[3]) - output_outputs) # 8x1
                    d_outs_d_nets = output_outputs*(1-output_outputs) # 8x1
                    d_error_d_nets = d_error_d_outs*d_outs_d_nets # 8x1
                    d_nets_d_weights = np.array([hidden_outputs]*OUTPUT_NEURONS) # 8x10

                    d_error_d_weights = (d_nets_d_weights.T * d_error_d_nets).T
                    
                    new_ol_weights = np.subtract(ol_weights, LEARNING_RATE*d_error_d_weights) # 8x10

                    # calculating the changes on the hidden layer weights

                    d_errors_d_hiddenouts = np.array([np.dot(d_error_d_nets, ol_weights[:,i]) for i in range(0, HIDDEN_NEURONS)])
                    d_outs_d_nets = hidden_outputs*(1-hidden_outputs)
                    d_error_d_nets = d_errors_d_hiddenouts*d_outs_d_nets
                    d_nets_d_weights = np.array([input_vals]*HIDDEN_NEURONS)

                    d_error_d_weights = (d_nets_d_weights.T * d_error_d_nets).T
                            
                    new_hl_weights = np.subtract(hl_weights, LEARNING_RATE*d_error_d_weights)

                    # assign new weights
                    hl_weights = new_hl_weights
                    ol_weights = new_ol_weights

        plt.plot(errors)
        plt.title("Training loss over a training session")
        plt.xlabel("Training iterations")
        plt.ylabel("Loss")
        plt.show(block=False)

        print()
        weights_filename = input("Enter the file name to save the weights to (no extension, leave blank to not save them): ")
        if weights_filename:
            np.savez(weights_filename, hl_weights=hl_weights, ol_weights=ol_weights)

    else:
        weights_filename = input("Enter the name of the weights file (including extension): ")
        hl_weights, ol_weights = import_weights(weights_filename)

    while True:
        print("\nEnter any one of the channels blank to exit the program")
        try:
            r = float(input("Enter R channel: "))/256.0
            g = float(input("Enter G channel: "))/256.0
            b = float(input("Enter B channel: "))/256.0
        except:
            break

        input_vals = np.array([r, g, b])

        output_outputs = forward_pass(input_vals, hl_weights, ol_weights)
        guessed_colour = arr_to_colour_name(output_outputs)
        print(f"Guessed colour: {guessed_colour}")
        print(f"Output array: {output_outputs}")
