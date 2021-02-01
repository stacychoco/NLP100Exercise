"""
nlp_ch5.py

NLP 100 Exercise

Chapter 5: Dependency Parsing

Author: Stacy Nguyen
"""

import spacy
from nltk.tokenize import word_tokenize


"""
* Demo of spacy:

nlp = spacy.load("en_core_web_sm")
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
"""


class Word:
    def __init__(self, text):
        nlp = spacy.load("en_core_web_sm")
        word = nlp(text)
        self.text = word.text
        self.lemma = word.lemma_
        self.pos = word.pos_


def convert_sentence(sentence):
    """
    Converts sentence to Word objects.
    :param sentence:
    :return: converted sentence
    """
    word_array = word_tokenize(sentence)

    for i in range(len(word_array)):
        word_object = Word(word_array[i])
        word_array[i] = word_object

    return word_array


if __name__ == '__main__':
    """
    40. Read the parse result (words)
    Design a class Word that represents a word. This class has three member variables, text (word surface), 
    lemma (lemma), and pos (part-of-speech). Represent a sentence as an array of instances of Word class. 
    Implement a program to load the parse result, and store the text as an array of sentences. 
    Show the object of the first sentence of the body of the article.
    """
    print(convert_sentence("I am a fish"))
