import Edge as ce
import Node as cn
import Visualizer as cv

class Net(object):
    def connect_layers(self, in_layer, out_layer):
        for i in in_layer:
            for o in out_layer:
                edge = ce.Edge(i, o)
                i.set_output(edge)
                o.set_input(edge)

    def __init__(self, inputs, hidden, outputs):
        self.input  = [cn.Node() for i in range(inputs)]
        self.hidden = [cn.Node() for i in range(hidden)]
        self.output = [cn.Node() for i in range(outputs)]
        
        bias = cn.Node()
        bias.value = 1.0
        self.input.append(bias)
                
        print "Created nodes"

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
