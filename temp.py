from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy
from PIL import Image, ImageOps
batch_size = 128
num_classes = 10
epochs = 2

# input image dimensions
img_rows, img_cols = 28, 28

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("X")
print(type(x_train[0]))
print(x_train[0])

print("Y")
print(y_train[0])
path = "./image.png"
img  = Image.open(path).convert('L')

print(" ")
img.show()
img = img.resize((28, 28))
print(" ")
img.show()
img = ImageOps.invert(img)
img.show()
img = list(img.getdata())
img = [img[offset:offset+28] for offset in range(0, 28*28, 28)]
print("Image data")
print(img)

img = numpy.array(img)
print(type(img))

print("---------------------")
print(img.shape)
print(type(img))
print("---------------------")
print(x_train[0].shape)
print(type(x_train[0]))
