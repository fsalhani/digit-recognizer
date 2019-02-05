import numpy as np


MNIST_SIZE = 28
COLOR_SCALE = 255

class Preprocessor:
	def image_to_mnist(self, image):
		pixel_array = self._aggregate_to_mnist_array(image)

		return self._reshape_data(pixel_array) / COLOR_SCALE

	def _reshape_data(self, pixel_array):
		return pixel_array.reshape(1, 1, MNIST_SIZE, MNIST_SIZE)

	def _get_group_sizes(self, image):
		image_width = len(image[0])
		image_height = len(image)

		return image_height // MNIST_SIZE, image_width // MNIST_SIZE

	def _aggregate_to_mnist_array(self, image):
		mnist_array = np.zeros([MNIST_SIZE, MNIST_SIZE])

		for i in range(MNIST_SIZE):
			for j in range(MNIST_SIZE):
				mnist_array[i][j] = self._calculate_mnist_pixel(image,i,j)

		return mnist_array

	def _calculate_mnist_pixel(self, image,line,column):
		group_height, group_width = self._get_group_sizes(image)

		rgb_sum = 0
		for i in range(group_height):
			for j in range(group_width):
				rgb_sum += sum(image[line*group_height+i][column*group_width+j])//len(image[line][column])

		return rgb_sum / (group_width * group_height)
