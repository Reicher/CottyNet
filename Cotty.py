import random

class Connection(object):
    def __init__(self, perceptron_1, perceptron_2):
        self.perceptron_1 = perceptron_1
        self.perceptron_2 = perceptron_2
        self.weight = random.uniform(0, 1)

    def get_value_for(self, querist):
        if querist is self.perceptron_1:
            return self.weight * self.perceptron_2.value
        elif querist is self.perceptron_2:
            return self.weight * self.perceptron_1.value
        else:
            print "Error: Asking for unconnected value"        

class Perceptron(object):
    def __init__(self):
        self.activation_threshold = 1.0
        self.value = 0.0
        self.input = []
        self.output = []
        
    def set_input(self, in_connection):
        self.input.append(in_connection)

    def set_output(self, out_connection):
        self.output.append(out_connection)
        
    def process(self):
        self.excitement = 0
        for i in self.input:
            self.excitement += i.get_value_for(self)
        
        if self.excitement >= self.activation_threshold:
            self.value = 1.0
        else:
            self.value = 0.0

        return self.value

class Net(object):
    def connect_layers(self, in_layer, out_layer):
        for i in in_layer:
            for o in out_layer:
                connection = Connection(i, o)
                i.set_output(connection)
                o.set_input(connection)

    def __init__(self, inputs, hidden, outputs):
        self.input  = [Perceptron() for i in range(inputs)]
        self.hidden = [Perceptron() for i in range(hidden)]
        self.output = [Perceptron() for i in range(outputs)]
        
        bias = Perceptron()
        bias.value = 1.0
        self.input.append(bias)
                
        print "Created perceptrons"

        self.connect_layers(self.input, self.hidden);
        self.connect_layers(self.hidden, self.hidden);
        self.connect_layers(self.hidden, self.output);
        print "Connected all layers"
        
        print "Created Cotty-net"

    def print_info(self):
        for i in self.input:
            print "Input have " + str(len(i.input)) + " inputs and " + str(len(i.output)) + " outputs. Value: " + str(i.value)

        for i in self.hidden:
            print "Hidden have " + str(len(i.input)) + " inputs  and " + str(len(i.output)) + " outputs. Value: " + str(i.value)

        for i in self.output:
            print "Output have " + str(len(i.input)) + " inputs and " + str(len(i.output)) + " outputs. Value: " + str(i.value)
            
    def run(self, input):
        for i in range(len(input)):
            self.input[i].value = input[i]

        for h in self.hidden:
            h.process()

        result = []
        for o in self.output:
            result.append(o.process())

        return result

    def train_one(self, input, output):
        print "Training with one example"

    def train_many(self, input_array, output_array):
        print "Training with many examples"        
