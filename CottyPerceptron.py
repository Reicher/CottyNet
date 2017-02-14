class Perceptron(object):
    def __init__(self):
        self.activation_threshold = 1.0
        self.value = 0.0
        self.input = []
        self.output = []
        
    def set_input(self, in_connection):
        self.input.append(in_connection)

    def set_output(self, out_connection):
        self.output.append(out_connection)
        
    def process(self):
        self.excitement = 0
        for i in self.input:
            self.excitement += i.get_value_for(self)
        
        if self.excitement >= self.activation_threshold:
            self.value = 1.0
        else:
            self.value = 0.0

        return self.value
