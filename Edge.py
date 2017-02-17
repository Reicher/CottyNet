import random

''' Connection between nodes with a weight'''
class Edge(object):
    def __init__(self, external_edge = False):
        self.weight = random.uniform(0, 1)
        self.value = 0.0
        self.external_edge = external_edge

    def set(self, value):
        self.value = self.weight * value

    def get(self):
        return self.value
