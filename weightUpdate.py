#!/usr/bin/env python
__author__ = 'will'

threshold = 0.5 # 0
learning_rate = .1  # 0.1
weights = [0, 0, 0]
# training set is a tuple containing 2 items: a tuple and an int
# 1st val: tuple: xi to xn where x is a potential input vector (the bias var must be present)
# 2nd val: int: is the desired output of the neural network
'''
training_set = [((1, -1, -1), 1),
                ((1, -1, 1), 1),
                ((1, 1, -1), 1),
                ((1, 1, 1), -1)]  # NAND with x0 as 1
'''
'''
training_set = [((-1, -1, -1), -1),
                ((-1, -1, 1), 1),
                ((-1, 1, -1), 1),
                ((-1, 1, 1), 1)]  # OR with x0 as -1; x0 is bias
'''
'''
training_set = [((1, -1, -1), -1),
                ((1, -1, 1), 1),
                ((1, 1, -1), 1),
                ((1, 1, 1), 1)]  # OR with x0 as 1
'''
training_set = [((1, 0, 0), 0),
                ((1, 0, 1), 1),
                ((1, 1, 0), 1),
                ((1, 1, 1), 1)] # OR with x0 as 1

def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))


while True:
    print('-' * 60)
    error_count = 0
    for input_vector, desired_output in training_set:
        print(weights)
        observed = 1 if dot_product(input_vector, weights) >= threshold else 0
        if observed != desired_output:
            error_count += 1
            for index, value in enumerate(input_vector):
                weights[index] += learning_rate * desired_output * value
    if error_count == 0:
        break
