import Edge

class Node(object):
    def __init__(self, id):
        self.id = id
        self.value = 0.0
        self.input = []
        self.output = []

    def add_input(self, in_edge):
        self.input.append(in_edge)

    def add_output(self, out_edge):
        self.output.append(out_edge)

    def sum_inputs(self):
        self.input_sum = 0.0
        for i in self.input:
            self.input_sum += i.get()

    def update_value(self):
        if self.input_sum >= 1.0:
            self.value = 1.0
        else:
            self.value = 0.0

        return self.value
