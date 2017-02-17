import Edge as ce
import Node as cn
import Net as net

def create_net( inputs, outputs ):
    tmp = net.Net()

    initial_nodes = inputs + outputs
    tmp.nodes  = [cn.Node(i) for i in range(initial_nodes)]
    for i in tmp.nodes:
        for j in tmp.nodes:
            e = ce.Edge()
            i.add_output(e)
            j.add_input(e)

    # Setup out and input edges and connect them to nodes.
    tmp.input  = [ce.Edge(True) for i in range(inputs)]
    for i in range(inputs):
        tmp.nodes[i].add_input(tmp.input[i])

    tmp.output = [ce.Edge(True) for o in range(outputs)]
    print len(tmp.nodes)
    for o in range(outputs):
        tmp.nodes[-o-1].add_output(tmp.output[i]) # a bit unclear?

    return tmp
