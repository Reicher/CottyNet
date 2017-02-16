import random

''' Connection between nodes with a weight'''
class Edge(object):
    def __init__(self):
        self.weight = random.uniform(0, 1)
        self.value = 0.0

    def set(self, value):
        self.value = self.weight * value

    def get(self):
        return self.value
