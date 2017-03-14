from numpy import exp, array, random, dot

class neural_network():
	def __init__(self):
		random.seed(1)
		self.weights = 2 * random.random((3,1)) - 1

	def sigmoid(self, z):
		return 1/(1+exp(-z))
		# z= X.WeightsT

	def predict(self, inputs):
		return self.sigmoid(dot(inputs, self.weights))

	def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
		

if __name__ == '__main__':

	#initialize single layer NN
	neural_network = neural_network()

	#random weights
	print('Random weights')
	print(neural_network.weights)

	training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
	training_set_outputs = array([0,1,1,0]).T

	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print('final weights')
	print(neural_network.weights)

