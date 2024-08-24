'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):  # passed
    mag_vec1 = 0
    for values in vec1.values():
        mag_vec1 = mag_vec1 + values**2
    mag_vec2 = 0
    for values in vec2.values():
        mag_vec2 = mag_vec2 + values**2
    dot_product = 0
    for key1 in vec1:
        if key1 in vec2:
            dot_product = dot_product + vec1[key1] * vec2[key1]
    return dot_product / (math.sqrt(mag_vec1) * math.sqrt(mag_vec2))


def build_semantic_descriptors(sentences):
    # make everything into one list
    jointed_everything = []
    for e in range(len(sentences)):
        for i in range(len(sentences[e])):
            jointed_everything.append(sentences[e][i])
    for words in jointed_everything:
        words = words.lower()
    # get a clean list
    clean_list = list(set(jointed_everything))
    # then for all the stuff in the clean list, it will be a key, then do ur stuff
    # first create a dictonary with the keys of all the stuff on clean list
    thedict = {}
    for words in clean_list:
        thedict[words] = None
    #crated a big dictonary for all the words
    # now im making independent dictionaries for each of the words in the clean list,
    for words in clean_list:
        for i in range(len(sentences)):
            if words in sentences[i]:



def build_semantic_descriptors_from_files(filenames):
    pass


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass


# testing
print(build_semantic_descriptors([["i", "am", "a", "sick", "man"],
                                  ["i", "am", "a", "spiteful", "man"],
                                  ["i", "am", "an", "unattractive", "man"],
                                  ["i", "believe", "my", "liver", "is", "diseased"],
                                  ["however", "i", "know", "nothing", "at", "all", "about", "my",
                                   "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]))
