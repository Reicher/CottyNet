# 2017 - CottyNet project
import Net as Cotty
import Visualizer as cv
import Trainer as pt

net = Cotty.Net(2, 2, 1)

cv.print_info(net)

input = [1, 1]
print "input: " + str(input) + " => " + str(net.run( input ))

#pt.train_one(net, [0, 1], [0])
