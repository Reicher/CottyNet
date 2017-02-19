def train_cycle(net, inputs, targets):
    for example in range(len(inputs)):
        output = net.run_until_stabile(inputs[example])
        error = []

        # Get errors for each example output
        for t in range(len(targets[example])):
            error.append(output['result'][t] - targets[example][t])

        # Feed each error to connected edges
        for o in range(len(net.output)):
            net.output[o].set_error(error[o])

        # Propegate the error around the net
        # for as if the net was serial connected
        for i in range(len(net.nodes)):
            for n in net.nodes:
                n.propegate_error()

    # After all examples are finished, update weights
    for i in net.nodes:
        i.update_weights()

    # Clear your mind to learn more, maaaan!
    net.clear_mind()

def train(net, inputs, targets):
    train_cycle(net, inputs, targets)
