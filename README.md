## Colour Recognizing Neural Network

This is a program that implements a feed-forward neural network to recognize colours by their RGB values.

I started on this project all the way back in 2017, but I didn't have the necessary math knowledge or skills to make it work successfully. Now, nearly 6 years later, I have made it work!

main.py has the actual network, backpropogation_example.ipynb is a Jupyter Notebook that I used to test out computational methods for the neural network (based on Matt Mazur's example, https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/), and generate_colours.py is a (flawed) automatic colour generation program written with the help of ChatGPT (which made a big mistake actually). colours.txt and generate_colours.txt are training data files with RGB values and colour names listed. colours.txt was the original file that I generated back in 2017 and colours_combined.txt is a larger file that I generated more recently with the help of a Processing application. weights.npz is a file with the weights from a training session, so import those if you want to use a pre-trained model.