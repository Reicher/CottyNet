def print_info(net):
    print "DEBUG INFO"
    for i in range(len(net.input)):
        print "Inputs" + " = " + str(net.input[i].get())

    for o in range(len(net.output)):
        print "Outputs" + " = " + str(net.input[o].get())

    for n in net.nodes:
        print "\nNode" + str(n.id) + " = " + str(n.value)
        print "Connections:"
        for i in n.input:
            special = "*" if i.external_edge else ""
            print "Input"+ special + " - w=" + str(i.weight) + " v=" + str(i.value)
        for o in n.output:
            special = "*" if o.external_edge else ""
            print "Output" + special + " - w=" + str(o.weight) + " v=" + str(o.value)
    print '\n'
