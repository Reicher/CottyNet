import random

''' Connection between nodes with a weight'''
class Edge(object):
    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = random.uniform(0, 1)

    ''' get value * weight from connected node '''
    def get_value_for(self, querist):
        return self.get_the_other(querist).value

    ''' get connected node'''
    def get_the_other(self, querist):
        if querist is self.node_1:
            return self.node_2
        elif querist is self.node_2:
            return self.node_1
        else:
            print "Error: Not connected"
