#!/usr/bin/env python
__author__ = 'will'


def init_font(file_name):
    """
    :rtype : tuple: (fontD, fontA, fontB, fontC)
    :param fileName: name of the file to be read
    :return : returns a tuple of "fonts" where each font is a list
    of # and . corresponding to the megaChar input
    """
    font_file = open(file_name)
    font1a = []
    font1b = []
    font1c = []
    font1d = []
    # order in file: D A B C
    for row in font_file:
        comps = row.split()
        font1d.extend(comps[0])
        font1a.extend(comps[1])
        font1b.extend(comps[2])
        font1c.extend(comps[3])
    font_file.close()
    # order in return: A B C D
    return font1a, font1b, font1c, font1d
#  end of initFont


def init_char(fileName):
    user_file = open(fileName)
    list_of_characters_in_mega_char = []
    for row in user_file:
        list_of_characters_in_mega_char.extend(row.strip("\n"))
    user_file.close()
    return list_of_characters_in_mega_char


def show_mega_char(mega_char):
    """
    prints out an entire character to the console.
    :param : list of ascii characters
    """
    iterations = 0
    line_of_mega_char = []
    for character in mega_char:
        iterations += 1
        line_of_mega_char.append(str(character))
        if iterations % 7 == 0:
            print("".join(line_of_mega_char))
            line_of_mega_char = []
# end of show_mega_char


def show_font_of_chars(font):
    """
    :param font: list of mega_chars, i.e. mega_char is a list of ascii chars
    """
    for mega_char in font:
        show_mega_char(mega_char)
        print ""


def input_vectorize_list_of_characters_and_add_bias(list_of_individual_characters):
    vectorToAdd = [1 if x == "#" else -1 for x in list_of_individual_characters]
    bias = 1
    vectorToAdd.append(bias)
    return vectorToAdd


def create_training_set_for_character(all_vectors, list_of_vectors_of_specific_character):
    """

    :param all_vectors: All of the vectors of all the characters ('A', 'B', 'C', 'D')
    :param list_of_vectors_of_specific_character: input vectors for a single character
    (i.e. vectors corresponding to 'A' or 'B' but not both.
    """
    training_set_for_specific_character = []
    for in_vec in all_vectors:
        vector_was_a_vector = False
        for character_vector in list_of_vectors_of_specific_character:
            if character_vector == in_vec:
                vector_was_a_vector = True
                break
        if vector_was_a_vector:
            training_set_for_specific_character.append((in_vec, 1))
        else:
            training_set_for_specific_character.append((in_vec, -1))
    return training_set_for_specific_character


def dot_product(values, weights):
    return sum(value * weight for value, weight in zip(values, weights))


def activation_function(input_vector, weights, threshold):
    return 1 if dot_product(input_vector, weights) >= threshold else -1


def weight_update(training_set, weights, threshold, learning_rate):
    """
    Trains the neural network by updating the weights
    :param training_set: a tuple with the first element an input vector
    (with the bias included) and the second element the desired output
    :param weights: the vector (list) of weights that must be updated
    so that the neural network is trained.
    """
    while True:
        error_count = 0
        for input_vector, desired_output in training_set:
            observed = activation_function(input_vector, weights, threshold)
            if desired_output != observed:
                error_count += 1
                for index, value in enumerate(input_vector):
                    weights[index] += learning_rate * desired_output * value
        if error_count == 0:
            break  # breaks out of while loop
'''
each font is a list of chars, i.e. [#, #, ., ., #, ....]
'''
font1 = list(init_font("zfont1"))
font2 = list(init_font("zfont2"))
font3 = list(init_font("zfont3"))

'''
each index of allChars contains a megaChar, i.e. [#, #, ., ., #, ....]
'''
allChars = []
allChars.extend(font1)
allChars.extend(font2)
allChars.extend(font3)

'''
Creates input_vectors, each being a numeric representation of a megaChar.
# will become 1, and . will become -1.  The bias(1) is appended to the end of each
input vector.  These are bipolar input vectors to be used in training the neural net.
'''
input_vectors = []
for index in range(len(allChars)):
    vectorToAdd = input_vectorize_list_of_characters_and_add_bias(allChars[index])
    input_vectors.append(vectorToAdd)
'''
creates individual vectors for each character to be recognized ('A', 'B', 'C', 'D')
'''
a_vectors = []
a_vectors.extend((input_vectors[0], input_vectors[4], input_vectors[8]))
b_vectors = []
b_vectors.extend((input_vectors[1], input_vectors[5], input_vectors[9]))
c_vectors = []
c_vectors.extend((input_vectors[2], input_vectors[6], input_vectors[10]))
d_vectors = []
d_vectors.extend((input_vectors[3], input_vectors[7], input_vectors[11]))

'''
Creates the training sets for each character
'''
a_training_set = create_training_set_for_character(input_vectors, a_vectors)
b_training_set = create_training_set_for_character(input_vectors, b_vectors)
c_training_set = create_training_set_for_character(input_vectors, c_vectors)
d_training_set = create_training_set_for_character(input_vectors, d_vectors)


'''
Initializes the weight vectors that correspond to the input vectors for a given character.
'''
length_of_each_input_vector = len(input_vectors[0])
initial_weight = 1
a_weights = [initial_weight for num in range(length_of_each_input_vector)]
b_weights = [initial_weight for num in range(length_of_each_input_vector)]
c_weights = [initial_weight for num in range(length_of_each_input_vector)]
d_weights = [initial_weight for num in range(length_of_each_input_vector)]

my_threshold = 0
my_learning_rate = .35

weight_update(a_training_set, a_weights, threshold=my_threshold, learning_rate=my_learning_rate)
weight_update(b_training_set, b_weights, threshold=my_threshold, learning_rate=my_learning_rate)
weight_update(c_training_set, c_weights, threshold=my_threshold, learning_rate=my_learning_rate)
weight_update(d_training_set, d_weights, threshold=my_threshold, learning_rate=my_learning_rate)

while True:
    fileName = raw_input("Type in file name of character to be identified." +
                         "\n Or press q to quit: ")

    if fileName != "q":
        user_char = init_char(fileName)
        show_mega_char(user_char)
        char_vector = input_vectorize_list_of_characters_and_add_bias(user_char)  # char_vector has bias
        # now I check if the activation function outputs a 1 for each of the neurons
        a_was_recognized = activation_function(char_vector, a_weights, threshold=my_threshold)
        b_was_recognized = activation_function(char_vector, b_weights, threshold=my_threshold)
        c_was_recognized = activation_function(char_vector, c_weights, threshold=my_threshold)
        d_was_recognized = activation_function(char_vector, d_weights, threshold=my_threshold)
        '''
        prints out the dot product of the user's chosen char vector and each weight
        print dot_product(char_vector, a_weights)
        print dot_product(char_vector, b_weights)
        print dot_product(char_vector, c_weights)
        print dot_product(char_vector, d_weights)
        '''
        if a_was_recognized == 1:
            print "Recognized as an \"A\""
        if b_was_recognized == 1:
            print "Recognized as a \"B\""
        if c_was_recognized == 1:
            print "Recognized as a \"C\""
        if d_was_recognized == 1:
            print "Recognized as a \"D\""
        if a_was_recognized != 1 and b_was_recognized != 1 and \
                c_was_recognized != 1 and d_was_recognized != 1:
            print "No neuron recognized this character"
    else:
        break
'''
# verification that the neural network at least recognizes the characters that
# it was trained to recognize
i = 0
weights = []
for vec in input_vectors:
    predicted = activation_function(vec, d_weights, my_threshold)
    if i % 4 == 0:
        print "A"
        weights = a_weights
    elif i % 4 == 1:
        print "B"
        weights = b_weights
    elif i % 4 == 2:
        print "C"
        weights = c_weights
    else:
        print "D"
        weights = d_weights
    print dot_product(vec, weights)

    if predicted == 1:
        print "was recognized"
    else:
        print "was not recognized"

    i += 1
'''