# 2017 - CottyNet project
import Cotty
import CottyVisualizer as cv
import CottyTrainer as pt

net = Cotty.Net(2, 2, 1)

cv.print_info(net)

#for i in range(10):
#    print net.run( [1, 1] )

pt.train_one(net, [0, 1], [0])
