def train_cycle(net, input, target):
    output = net.run_until_stabile(input)
    error = [abs(output['result'][i] - target[i]) for i in range(len(target))]

    [net.output[o].set_error(error[o]) for o in range(len(net.output))]

    # propegate the error as if the all nodes where in serial.
    for i in range(len(net.nodes)):
        for n in net.nodes:
            n.propegate_error()

    for n in net.nodes:
        n.update_weights()

def train(net, input, output, cycles):
    for i in range(cycles):
        train_cycle(net, input, output)
