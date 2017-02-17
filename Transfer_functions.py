import math

def step( weighted_sum, threshold ):
    return weighted_sum >= threshold

def linear_combination( weighted_sum, bias ):
    return weighted_sum + bias

def sigmoid( weighted_sum ):
    return weighted_sum / math.sqrt(1 + weighted_sum * weighted_sum)
