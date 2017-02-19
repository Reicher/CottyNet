# 2017 - CottyNet project
import Net as Cotty
import Visualizer as cv
import Trainer as pt
import Builder as cb

from random import randint
import time

input = [[0, 1],[1, 0], [0, 0], [1, 1]]
target = [[0], [0], [0], [1]]
net = cb.create_net(2, 0, 1)

while True:
    print(chr(27) + "[2J")

    pt.train(net, input, target)
    for i in input:
        print '\n' + str(i)
        result = net.run_until_stabile(i)
        print result['result']


    time.sleep(0.1)

# cv.print_info(net)
#
