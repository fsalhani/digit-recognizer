import numpy as np


MNIST_WIDTH = 28
MNIST_HEIGHT = 28
COLOR_SCALE = 255

class Preprocessor:
	def reshape_data(pixel_array):
		return pixel_array.reshape(1, 1, MNIST_WIDTH, MNIST_HEIGHT) / COLOR_SCALE
