def print_info(net):
    print "DEBUG INFO"
    for i in range(len(net.input)):
        print "Input" + str(i) + " = " + str(net.input[i].get())

    for o in range(len(net.output)):
        print "Output" + str(o) + " = " + str(net.output[o].get())

    for n in net.nodes:
        print "\nNode" + str(n.id) + " = " + str(n.value) + (" (bias)" if n.bias else "")
        print "Connections:"
        for i in n.input:
            special = "*" if i.external_edge else ""
            print "Input"+ special + " - w=" + str(i.weight) + " v=" + str(i.value)
        for o in n.output:
            special = "*" if o.external_edge else ""
            print "Output" + special + " - w=" + str(o.weight) + " v=" + str(o.value)
    print '\n'
