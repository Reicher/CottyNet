def train_one(net, input, target):
    output = net.run_until_stabile(input)
    error = [abs(output['result'][i] - target[i]) for i in range(len(target))]
    print error
    print "Trained with one example"

def train(input_array, output_array):
    print "Training with many examples"
