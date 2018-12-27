import pickle

from .preprocessor import Preprocessor

class Predictor:
	_model = None

	def _load_model(self):
		filename = 'akangatu/model/model.pkl'

		with open(filename, 'rb') as f:
			self._model = pickle.load(f)

	def predict(self, pixel_array):
		if not self._model:
			self._load_model()

		pixels = Preprocessor.image_to_mnist(pixel_array)

		probs = self._model.predict(pixels)
		return probs.argmax(axis=1)
