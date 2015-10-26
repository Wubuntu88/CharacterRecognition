#!/usr/bin/env python
__author__ = 'will'

threshold = 0  # 0.5
learning_rate = 1  # 0.1
weights = [0, 0, 0]
training_set = [((1, -1, -1), 1),
                ((1, -1, 1), 1),
                ((1, 1, -1), 1),
                ((1, 1, 1), -1)]  # NAND
#  training_set = [((-1, -1, -1), -1), ((-1, -1, 1), 1), ((-1, 1, -1), 1), ((-1, 1, 1), 1)] #  OR


def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))


while True:
    print('-' * 60)
    error_count = 0
    for input_vector, desired_output in training_set:
        print(weights)
        observed = 1 if dot_product(input_vector, weights) >= threshold else -1
        if observed != desired_output:
            error_count += 1
            for index, value in enumerate(input_vector):
                weights[index] += learning_rate * desired_output * value
    if error_count == 0:
        break
