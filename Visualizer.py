def print_info(net):
    print "DEBUG INFO"
    for i in range(len(net.input)):
        print "Inputs" + str(i) + " = " + str(net.input[i].get())

    for n in net.nodes:
        print "\nNode" + str(n.id) + " = " + str(n.value)
        print "Connections:"
        for i in n.input:
            print "Input - w=" + str(i.weight) + " v=" + str(i.value)
        for o in n.output:
            print "Output - w=" + str(o.weight) + " v=" + str(o.value)
    print '\n'
