# 2017 - CottyNet project
import Net as Cotty
import Visualizer as cv
import Trainer as pt
import Builder as cb

net = cb.create_net(1, 1)

#cv.print_info(net)

input = [1]
print "input: " + str(input) + \
    " => " + str(net.run_cycle( input ))

#pt.train_one(net, [0, 1], [0])
