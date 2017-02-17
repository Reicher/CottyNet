import Edge
import Transfer_functions
import random

# Process should be in 3 steps
# 1. Collect - Collect/sum all (weighted)values from input-connections
# 2. Process - Depending on Sum and activationfunktion, activate node
# 3. Distribute - Set node value to all output-connections

class Node(object):
    def __init__(self, id):
        self.id = id
        self.value = random.uniform(0, 1)
        self.input = []
        self.output = []

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
        self.value = Transfer_functions.sigmoid(self.weighted_sum)

    ''' Update all output edges with your new value '''
    def distribute(self):
        for o in self.output:
            o.set(self.value)
