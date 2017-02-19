import math

def step( weighted_sum, threshold ):
    return weighted_sum >= threshold

def linear_combination( weighted_sum, bias ):
    return weighted_sum + bias

def sigmoid( x ):
    return 1 / (1 + math.exp(-x))
