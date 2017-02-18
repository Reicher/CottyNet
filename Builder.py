import Edge as ce
import Node as cn
import Net as net

def create_net( inputs, hidden, outputs ):
    tmp = net.Net()

    initial_nodes = inputs + hidden + outputs
    bias = cn.Node(0, bias=True) # Create bias node
    tmp.nodes  = [cn.Node(i+1) for i in range(initial_nodes)]
    for i in tmp.nodes:
        bias_e = ce.Edge()
        bias.add_output(bias_e)
        i.add_input(bias_e)
        for j in tmp.nodes:
            e = ce.Edge()
            i.add_output(e)
            j.add_input(e)

    tmp.nodes.append(bias)
    # Setup out and input edges and connect them to nodes.
    tmp.input  = [ce.Edge(True) for i in range(inputs)]
    for i in range(inputs):
        tmp.nodes[i].add_input(tmp.input[i])

    tmp.output = [ce.Edge(True) for o in range(outputs)]
    for o in range(outputs):
        tmp.nodes[inputs+o].add_output(tmp.output[o]) # a bit unclear?

    return tmp
