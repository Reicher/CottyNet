import Edge
import Transfer_functions
import random

# Process should be in 3 steps
# 1. Collect - Collect/sum all (weighted)values from input-connections
# 2. Process - Depending on Sum and activationfunktion, activate node
# 3. Distribute - Set node value to all output-connections

class Node(object):
    def __init__(self, id, bias = False):
        self.id = id
        self.value = random.uniform(0, 1)
        self.input = []
        self.output = []
        self.bias = bias

        self.weighted_sum = 0.0
        self.error = 0.0

    def clear(self):
        self.value = random.uniform(0, 1)
        self.error = 0.0
        self.weighted_sum = 0.0

        for i in self.input:
            i.clear()

        for o in self.output:
            o.clear()

    def add_input(self, in_edge):
        self.input.append(in_edge)

    def add_output(self, out_edge):
        self.output.append(out_edge)

    ''' Collect/sum all (weighted)values from input-connections '''
    def collect(self):
        self.weighted_sum = 0.0
        for i in self.input:
            self.weighted_sum += i.get()

    ''' Run transfer function on weighted sum'''
    def process(self):
        if not self.bias:
            self.value = Transfer_functions.sigmoid(self.weighted_sum)
        else:
            self.value = 1.0

    ''' Update all output edges with your new value '''
    def distribute(self):
        for o in self.output:
            o.set(self.value)

    def propegate_error(self):
        for o in self.output:
            self.error += o.get_error()

        for i in self.input:
            i.set_error(self.error)

    def update_weights(self):
        transfer_error = Transfer_functions.sigmoid(self.error)
        learning_rate = 0.1
        der_error = transfer_error * (1 -  transfer_error)
        for i in self.input:
            i.weight += learning_rate * der_error
