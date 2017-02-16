def print_info(net):
    for i in net.input:
        print "Input" +str(i.id) + " have " + str(len(i.input)) + " inputs and " + str(len(i.output)) + " outputs. Value: " + str(i.value)

    for i in net.hidden:
        print "Hidden" + str(i.id) + " have " + str(len(i.input)) + " inputs  and " + str(len(i.output)) + " outputs. Value: " + str(i.value)

    for i in net.output:
        print "Output"  + str(i.id) + " have " + str(len(i.input)) + " inputs and " + str(len(i.output)) + " outputs. Value: " + str(i.value)
    
