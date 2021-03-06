import numpy as np 
import scipy.special

class Nnet():

	def __init__(self, num_input, num_hidden, num_output):
		self.num_input = num_input
		self.num_hidden = num_hidden
		self.num_output = num_output
		self.weight_input_hidden = np.random.uniform(-0.5, 0.5, size=(self.num_hidden,self.num_input))
		self.weight_hidden_output = np.random.uniform(-0.5, 0.5, size=(self.num_output,self.num_hidden))
		self.activation_function = lambda x: scipy.special.expit(x)

	def get_outputs(self, inputs_list):
		inputs = np.array(inputs_list, ndmin=2).T
		#print("Inputs: ", inputs, sep="\n")
		hidden_inputs = np.dot(self.weight_input_hidden, inputs)
		#print("Hidden Inputs: ", hidden_inputs, sep="\n")
		hidden_outputs = self.activation_function(hidden_inputs)
		#print("Hidden Outputs: ", hidden_outputs, sep="\n")
		final_inputs = np.dot(self.weight_hidden_output, hidden_outputs)
		#print("Final Inputs: ", final_inputs, sep="\n")
		final_outputs = self.activation_function(final_inputs)
		#print("Final Outputs: ", final_outputs, sep="\n")
		return final_outputs

	def get_max_value(self, inputs_list):
		outputs = self.get_outputs(inputs_list)
		return np.max(outputs)

def tests():
	nnet = Nnet(2,5,2)
	print("weight_input_hidden", nnet.weight_input_hidden, sep="\n")
	print("weight_hidden_output", nnet.weight_hidden_output, sep="\n")

	inputs = [0.2, 0.6]
	output = nnet.get_max_value(inputs)
	print("output", output, sep="\n")

if __name__ == "__main__":
	#tests()