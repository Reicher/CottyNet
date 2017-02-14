import Connection as cc
import Perceptron as cp
import Visualizer as cv

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

        cycles = 0
        cycles_stable = 0
        cycles_min = len(self.hidden)
        cycles_max = len(self.hidden) * 100 # or something?        

        result = []
        while cycles_stable < cycles_min:
            last_cycle_result = result
            result = []
            for i in range(len(input)):
                self.input[i].value = input[i]

            for h in self.hidden:
                h.process()
            
            for o in self.output:
                result.append(o.process())

            if result == last_cycle_result:
                cycles_stable += 1
            else:
                cycles_stable = 0

            cycles += 1
            if cycles >= cycles_max:
                print "Cotty is not sure.."
                return

        return result        
