# Colour Recognizing Neural Network

This is a program that implements a feed-forward neural network to recognize colours by their RGB values.

I started on this project all the way back in 2018, but I didn't have the necessary math knowledge or skills to make it work successfully. Now, nearly 5 years later, I have made it work!

## Contents
- `main.py` has the actual network
- `backpropogation_example.ipynb` is a Jupyter Notebook that I used to test out computational methods for the neural network (based on [Matt Mazur's example](https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/))
- `generate_colours.py` is a (flawed) automatic colour generation program written with the help of ChatGPT (which made a big mistake actually, because it made yellow and orange the same colour)
- `ColourClassifier/ColourClassifier.pde` is a processing application that allows me to quickly generate a training data file
- `colours.txt` and `generate_colours.txt` are training data files with RGB values and colour names listed
    - `colours.txt` was the original file that I generated back in 2017
    - `colours_combined.txt` is a larger file that I generated more recently with the help of the Processing application ColourClassifier
- `weights.npz` is a file with the weights from a training session, so import those if you want to use a pre-trained model

## Dependencies

### Python scripts
- Python 3 (could probably run with lots of different versions, but I wrote it using 3.10)
- NumPy (again, probably has a wide range of versions that you could use, but I'm using 1.23)
- Matplotlib (same as above, I'm using 3.5)

### Processing program
- Processing (could probably use 3 or 4, but I used 4)

## Usage

- Running the main network: `python main.py`  
    - Make sure you set the properties in the program before running it  
- Running the Jupyter notebook: in a command prompt or terminal, `cd` into wherever this directory is downloaded and run `jupyter notebook`  
- Running the Processing program: open `ColourClassifier.pde` in the Processing IDE (within its folder) and click the run button  
    - Make sure you set the properties in the program before running it  

## Properties in main.py

- `INPUT_NEURONS` - number of neurons in the input layer. Depends on what data format your input is
- `HIDDEN_NEURONS` - number of neurons in the hidden layer. The only real independent variable affecting how capable the network is. Should not be too low such that it can't complete the task and not to high such that it will remember the training data and overfit
- `OUTPUT_NEURONS` - number of neurons in the output layer. Depends on what data format your output is
- `TRAINING_FILE_NAME` - name of the file that you use for your training data
- `EPOCHS` - number of full pass-throughs of the training data the network will do during training
- `TRAIN` - boolean variable that says whether or not to train the network or just run the network with pre-existing weights
- `LEARNING_RATE` - set the learning rate of the network