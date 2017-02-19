import random

''' Connection between nodes with a weight'''
class Edge(object):
    def __init__(self, external_edge = False):
        self.value = 0.0
        self.d_error = 0.0

        self.external_edge = external_edge
        self.weight = random.uniform(0, 1)

    def clear(self):
        self.d_error = 0.0
        self.value = 0.0

    def set(self, value):
        self.value = self.weight * value

    def get(self):
        if self.external_edge:
            return self.weight
        else:
            return self.value

    def set_error(self, delta_error):
        self.d_error = delta_error

    def get_error(self):
        return self.d_error * self.weight
        clear()
