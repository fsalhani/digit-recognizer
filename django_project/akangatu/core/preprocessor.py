import numpy as np


MNIST_SIZE = 28
COLOR_SCALE = 255

class Preprocessor:
	def image_to_mnist(image):
		pixel_array = aggregate_to_mnist_array(image)

		return reshape_data(pixel_array) / COLOR_SCALE

	def reshape_data(pixel_array):
		return pixel_array.reshape(1, 1, MNIST_SIZE, MNIST_SIZE)

	def get_group_sizes(image):
		image_width = len(image[0])
		image_height = len(image)

		return image_height // MNIST_SIZE, image_width // MNIST_SIZE

	def aggregate_to_mnist_array(image):
		mnist_array = np.zeros([MNIST_SIZE, MNIST_SIZE])

		for i in range(MNIST_SIZE):
			for j in range(MNIST_SIZE):
				pixel_array[i][j] = calculate_mnist_pixel(image,i,j)

		return mnist_array

	def calculate_mnist_pixel(image,line,column):
		group_height, group_width = get_group_sizes(image)

		rgb_sum = 0
		for i in range(group_height):
			for j in range(group_width):
				rgb_sum += sum(image[line*group_height+i][column*group_width+l])//len(image[line][column])

		return rgb_sum / (group_width * group_height)
