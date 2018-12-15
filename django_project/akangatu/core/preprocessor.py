import numpy as np

class Preprocessor:
	def reshape_data(request):
		pixel_array = np.array(request)
		return pixel_array.reshape(-1, 1, 28, 28) / 255.0
