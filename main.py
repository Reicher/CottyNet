# 2017 - CottyNet project
import Net as Cotty
import Visualizer as cv
import Trainer as pt
import Builder as cb

from random import randint
import time

while True:
    input = [randint(0,1)]
    net = cb.create_net(1,randint(0,10), 3)
    output = net.run_until_stabile(input)
    print "Result: " + str(output['result']) + " with " + str(len(net.nodes)) + " nodes after " + str(output['cycles']) + " cycles."
    time.sleep(1)

# cv.print_info(net)
#pt.train_one(net, [1], [1, 1])
