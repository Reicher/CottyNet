# 2017 - CottyNet project
import Cotty

net = Cotty.Net(2, 2, 1)

#net.print_info()

for i in range(10):
    print net.run( [1, 1] )
