def print_info(net):
    for i in net.input:
        print "Input have " + str(len(i.input)) + " inputs and " + str(len(i.output)) + " outputs. Value: " + str(i.value)

    for i in net.hidden:
        print "Hidden have " + str(len(i.input)) + " inputs  and " + str(len(i.output)) + " outputs. Value: " + str(i.value)

    for i in net.output:
        print "Output have " + str(len(i.input)) + " inputs and " + str(len(i.output)) + " outputs. Value: " + str(i.value)
    
