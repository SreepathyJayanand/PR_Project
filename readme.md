## How to execute the project
Run app.py (It predicts based on the pretrained weights that we have generated and stored in "Trained_weights.hdf5")

Wait for app.py to detect the image you drew in the canvas

See the output in the message box

## How to train
Execute [CNN_mnist.py](CNN_mnist.py)

The saved weights file are stored in Trained_weights.hdf5

## Documentation
Language - Python (3.7.7)

Neural Network library - Keras (2.4.3)

Computational library - Numpy (1.18.2)

Graphic Library - Tkinter (8.5)

Image Library - Pillow (6.2.1)

Model used - Sequential(Each layer has 1 input tensor and 1 output tensor)

Loss funtion - Categorical cross entropy loss(Softmax/normalized_exponential_funtion + cross_entropy_loss)

Optimizer - Adadelta(Advanced Gradient descent without the drawback of decaying learning rate throughout training and without the need of giving an expicit learning rate)

Epochs - 10

Batch size for training - 128

Dataset used - MNIST with each image being 28 x 28 pixels

### Image specifications

Total images = 70000 split into 60000 for training and 10000 for testing

Input for training - (60000, 28, 28, 1) tensor

Input for testing - (10000, 28, 28, 1) tensor

### Feature Extraction part:

The first convolutional layer has 32 filters each of size 3 x 3
and activation function used is ReLu and takes the 28 x 28 image as input

The second convolutional layer has 64 filters each of size 3 x 3 and activation function used is again ReLu

Then we add a maxpooling layer with a window/pool size of 2 x 2

We add a dropout function to prevent overfitting such that each node randomly gets weights of 0 with a probability of 0.25

### Learning part:

First we flatten to make the 2d array which we processed so far to make it 1d for passing it on to the dense fully connected layer.

We add a dense layer for our network which is a fully connected layer with 128 nodes.

Again we add a dropout funtion to prevent overfitting with each node having a probability of 0.5 to get a weight of 0.

Finally we again add a dense layer of 10 nodes which receives input from the 128 nodes in the previous layer with the softmax activation function and converts it to an answer from 0 - 9.
test













