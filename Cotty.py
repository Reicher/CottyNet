import CottyConnection as cc
import CottyPerceptron as cp
import CottyVisualizer as cv

class Net(object):
    def connect_layers(self, in_layer, out_layer):
        for i in in_layer:
            for o in out_layer:
                connection = cc.Connection(i, o)
                i.set_output(connection)
                o.set_input(connection)

    def __init__(self, inputs, hidden, outputs):
        self.input  = [cp.Perceptron() for i in range(inputs)]
        self.hidden = [cp.Perceptron() for i in range(hidden)]
        self.output = [cp.Perceptron() for i in range(outputs)]
        
        bias = cp.Perceptron()
        bias.value = 1.0
        self.input.append(bias)
                
        print "Created perceptrons"

        self.connect_layers(self.input, self.hidden);
        self.connect_layers(self.hidden, self.hidden);
        self.connect_layers(self.hidden, self.output);
        print "Connected all layers"
        
        print "Created Cotty-net"
        
    def run(self, input):
        for i in range(len(input)):
            self.input[i].value = input[i]

        for h in self.hidden:
            h.process()

        result = []
        for o in self.output:
            result.append(o.process())

        return result        
