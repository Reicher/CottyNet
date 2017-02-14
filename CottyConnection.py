import random

class Connection(object):
    def __init__(self, perceptron_1, perceptron_2):
        self.perceptron_1 = perceptron_1
        self.perceptron_2 = perceptron_2
        self.weight = random.uniform(0, 1)

    def get_value_for(self, querist):
        return self.get_the_other(querist).value

    def get_the_other(self, querist):
        if querist is self.perceptron_1:
            return self.perceptron_2
        elif querist is self.perceptron_2:
            return self.perceptron_1
        else:
            print "Error: Not connected"
