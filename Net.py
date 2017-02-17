import Edge as ce
import Node as cn
import Visualizer as cv

class Net(object):
    def run_cycle(self, input):
        # Set static input values
        for i in range(len(input)):
            self.input[i].value = input[i]

        #cv.print_info(self)

        # Update whole net
        for n in self.nodes:
            n.collect()
            n.process()

        for n in self.nodes:
            n.distribute()

        return {'result': [out.get() for out in self.output], 'cycles': 1}

    def run_until_stabile(self, input):
        last_output = {'result': [], 'cycles': 0}
        cycles = 1
        output = self.run_cycle(input)

        while output['result'] != last_output['result']:
            cycles += 1
            last_output = output
            output = self.run_cycle(input)
            print output['result']


        return  {'result': output['result'], 'cycles': cycles}
