import random

''' Connection between nodes with a weight'''
class Edge(object):
    def __init__(self, external_edge = False):
        self.value = 0.0
        self.d_error = 0.0

        self.external_edge = external_edge
        if self.external_edge:
            self.weight = random.uniform(0, 1)
        else:
            self.weight = 1.0

    def set(self, value):
        self.value = self.weight * value

    def get(self):
        return self.value

    def set_error(self, delta_error):
        self.d_error = delta_error
