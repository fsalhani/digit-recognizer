import pickle

class Predictor:
	_model = None

	def load_model(self):
		filename = 

		with open(filename, 'rb') as f:
			self._model = pickle.load(f)

	def predict(self, pixels):
		if not self._model:
			load_model()

		probs = self._model.predict(pixels)
		return probs.argmax(axis=1)
