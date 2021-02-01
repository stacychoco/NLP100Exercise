"""
nlp_ch5.py

NLP 100 Exercise

Chapter 5: Dependency Parsing

Author: Stacy Nguyen
"""

import spacy

# Demo of spacy module:
"""
nlp = spacy.load("en_core_web_sm")
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
"""


class Word:
    def __init__(self, text, lemma="", pos=""):
        self.text = text
        self.lemma = lemma
        self.pos = pos


def load_parse_result(sentence):
    nlp = spacy.load("en_core_web_sm")
    data = nlp(sentence)
    return data


def convert_sentence(sentence):
    """
    Converts sentence to Word objects.
    :param sentence:
    :return: converted sentence
    """
    data = load_parse_result(sentence)
    word_array = []
    for token in data:
        word_array.append(Word(token.text, token.lemma_, token.pos_))
    return word_array


if __name__ == '__main__':
    """
    40. Read the parse result (words)
    Design a class Word that represents a word. This class has three member variables, text (word surface), 
    lemma (lemma), and pos (part-of-speech). Represent a sentence as an array of instances of Word class. 
    Implement a program to load the parse result, and store the text as an array of sentences. 
    Show the object of the first sentence of the body of the article.
    """
    # This sentence is now represented as a list of Word objects
    converted_sentence = convert_sentence("Sometimes, people become superheroes.")
    for object in converted_sentence:
        print(object.text, object.lemma, object.pos)

    # Represent article as a list of sentences
    # Output the first sentence of the text
