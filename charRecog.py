#!/usr/bin/env python
__author__ = 'will'


def init_font(file_name):
    """
    :rtype : tuple: (fontD, fontA, fontB, fontC)
    :param fileName: name of the file to be read
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

font1 = list(init_font("zfont1"))
font2 = list(init_font("zfont2"))
font3 = list(init_font("zfont3"))

allChars = []
allChars.extend(font1)
allChars.extend(font2)
allChars.extend(font3)

input_vectors = []
for index in range(len(allChars)):
    vectorToAdd = [1 if x == "#" else 0 for x in allChars[index]]
    bias = -1
    vectorToAdd.append(bias)
    input_vectors.append(vectorToAdd)

a_vectors = []
a_vectors.extend((input_vectors[0], input_vectors[4], input_vectors[8]))
b_vectors = []
b_vectors.extend((input_vectors[1], input_vectors[5], input_vectors[9]))
c_vectors = []
c_vectors.extend((input_vectors[2], input_vectors[6], input_vectors[10]))
d_vectors = []
d_vectors.extend((input_vectors[3], input_vectors[7], input_vectors[11]))



threshold = 0.5
learning_rate = 1
length_of_each_input_vector = len(input_vectors[0])
a_weights = [0 for num in range(length_of_each_input_vector)]
b_weights = [0 for num in range(length_of_each_input_vector)]
c_weights = [0 for num in range(length_of_each_input_vector)]
d_weights = [0 for num in range(length_of_each_input_vector)]

# now I must create the training set for each neuron, i.e. the neuron that recognizes "A"
# the neuron that recognizes "B", etc.  For example, the training set for "A" will
# have the input vectors of as well as the input vectors for all of the other vectors
# ("B", "C", and "D").  Desired output for "A" input vectors will have a desired output of 1
# while the other input vectors will have the desired output of 0.  This is for neuron "A".















