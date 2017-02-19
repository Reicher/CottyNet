import Edge as ce
import Node as cn
import Visualizer as cv

class Net(object):
    def clear_mind(self):
        for n in self.nodes:
            n.clear()

    def run_cycle(self, input):
        # Set static input values
        for i in range(len(input)):
            self.input[i].value = input[i]

        # Update whole net
        for n in self.nodes:
            n.collect()
            n.process()

        for n in self.nodes:
            n.distribute()

        return {'result': [out.get() for out in self.output], 'cycles': 1}

    def run_cycles(self, input, cycles):
        return [self.run_cycle(input) for i in range(cycles)]

    def run_until_stabile(self, input):
        last_output = {'result': [], 'cycles': 0}
        cycles = 1
        max_cycles = 5000
        output = self.run_cycle(input)

        while output['result'] != last_output['result']:
            if cycles >= max_cycles:
                return {'result': [0.0], 'cycles': cycles}

            cycles += 1
            last_output = output
            output = self.run_cycle(input)

        return  {'result': output['result'], 'cycles': cycles}
