import Edge as ce
import Node as cn
import Visualizer as cv

class Net(object):
    def run_cycle(self, input):
        result = []

        # Set static input values
        for i in range(len(input)):
            self.input[i].value = input[i]

        cv.print_info(self)

        # Set values in net
        for n in self.nodes:
            n.sum_inputs()

        for n in self.nodes:
            n.update_value()

        result = [out.get() for out in self.output]

        return result
