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


def cosine_similarity(vec1, vec2):
    same_word = 0
    mag1 = 0
    mag2 = 0
    for i in vec1:
        if i in vec2:
            same_word += vec1[i] * vec2[i]
        mag1 += vec1[i]**2
    for i in vec2:
        mag2 += vec2[i]**2
    similarity = same_word/math.sqrt(mag1*mag2)
    return similarity


def build_semantic_descriptors(sentences):
    d = {}
    for sent in sentences:  # each sentence
        for w in sent:  # each word
            if w not in d:  # for new word
                d[w] = {}  # new entry for word, a dictionary for other words in sentence
            for i in sent:  # check words in sentence
                if i != w:
                    if i not in d[w]:
                        d[w][i] = 1  # new entry
                    else:
                        d[w][i] += 1  # add to existing entry
    return d


def build_semantic_descriptors_from_files(filenames):

    file = open(filenames[0], "r", encoding="latin1").read()

    file.replace("!", ".")  # All punctuation for sentences becomes uniform "."
    file.replace("?", ".")

    file.replace(",", " ")  # All word separators replaced by space
    file.replace("--", " ")  # first double, then single dash
    file.replace("-", " ")
    file.replace(":", " ")
    file.replace(";", " ")

    sentences = []
    for i in file.split("."):  # sentence1, sentence2
        phrase = []
        for word in i.split():
            phrase.append(word)
        # phrase = [i] #[phrase1], [phrase2]
        sentences.append(phrase)  # each sentence, list of sentence

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    if not choices:
        return None
    similarity_list = []
    for choice in choices[0:]:
        similarity = similarity_fn(semantic_descriptors.get(
            word, {}), semantic_descriptors.get(choice, {}))
        similarity_list.append(similarity)
    return choices[similarity_list.index(max(similarity_list))]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    file = open(filename, "r", encoding="latin1")


if __name__ == "__main__":
    # text = [["i", "am", "a", "sick", "man"],
    # ["i", "am", "a", "spiteful","man"],
    # ["i", "am", "an", "unattractive", "man"],
    # ["i", "believe", "my", "liver", "is", "diseased"],
    # ["however", "i", "know", "nothing", "at", "all", "about", "my",
    # "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]

    filenames = ["war_and_peace.txt"]
    # print(build_semantic_descriptors(text))
    print(build_semantic_descriptors_from_files(filenames))
