# 2017 - CottyNet project
import Net as Cotty
import Visualizer as cv
import Trainer as pt
import Builder as cb

from random import randint
import time

while True:
    input = [randint(0,5)]
    target = [randint(0,5)]

    net = cb.create_net(1,randint(0,10), 1)

    pt.train(net, input, target, 1000)

    output = net.run_until_stabile(input)

    diff = target[0] - output['result'][0]

    print "Result: " + str(output['result']) + " with " + str(len(net.nodes)) + " nodes after " + str(output['cycles']) + " cycles."
    print "Diff: " + str(diff) + '\n'
    time.sleep(1)

# cv.print_info(net)
#
