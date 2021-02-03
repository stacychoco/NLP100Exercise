"""
nlp_ch5.py

NLP 100 Exercise

Chapter 5: Dependency Parsing

Author: Stacy Nguyen
"""

import spacy
from nltk.tokenize import sent_tokenize

# Demo of spacy module:
"""
nlp = spacy.load("en_core_web_sm")
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
"""


class Word:
    def __init__(self, text, lemma="", pos="", head="", dep="", children=[]):
        self.text = text
        self.lemma = lemma
        self.pos = pos
        self.head = head
        self.dep = dep
        self.children = children


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
        word_array.append(Word(token.text, token.lemma_, token.pos_,
                               token.head, token.dep_,
                               [child for child in token.children]))
    return word_array


if __name__ == '__main__':
    """
    40. Read the parse result (words)
    Design a class Word that represents a word. This class has three member variables, text (word surface), 
    lemma (lemma), and pos (part-of-speech). Represent a sentence as an array of instances of Word class. 
    Implement a program to load the parse result, and store the text as an array of sentences. 
    Show the object of the first sentence of the body of the article.
    
    41. Read the parse result (dependency)
    In addition to problem 40, add three member variables head (a reference to the object of its 
    syntactic governor), dep (dependency type to its governor), and children (a list of references 
    to the syntactic dependents in the parse tree) to the class Word. Show the pairs of governors 
    (parents) and their dependents (children) of the first sentence of the body of the article. 
    Use the class Word in the rest of the problems in this chapter.
    """
    # Represent article as a list of sentences
    with open("ai.en/ai.en.txt", 'r') as file:
        article = file.read()
    tokenized_article = sent_tokenize(article)

    # Output the first sentence of the text as a list of objects
    first_sentence = tokenized_article[0]

    # This sentence is now represented as a list of Word objects
    converted_sentence = convert_sentence(first_sentence)
    for object in converted_sentence:
        # problem 40: text, lemma, pos
        # problem 41: head, dep, children
        print(object.text, object.lemma, object.pos,
              object.head, object.dep, object.children)
