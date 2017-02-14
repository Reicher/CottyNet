def train_one(net, input, target):
    #max_response_time = 0
    max_cycles = 10
    cycles = 0
    
    while net.run(input) != target and cycles < max_cycles:
        cycles += 1
        delta_error = []                           
        print "training cycle " + str(cycles)
            
    print "Trained with one example"        

def train_many(input_array, output_array):
    print "Training with many examples"
