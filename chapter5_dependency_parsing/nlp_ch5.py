"""
nlp_ch5.py

NLP 100 Exercise

Chapter 5: Dependency Parsing

Author: Stacy Nguyen
"""

import spacy
from nltk.tokenize import sent_tokenize


# ***Demo of spacy module:***
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
# for token in doc:
#     print(token.text, token.dep_, token.head.text, token.head.pos_,
#             [child for child in token.children])


class Word:
    def __init__(self, text, lemma="", pos="", tag="", head="", dep="", children=None):
        if children is None:
            children = []
        self.text = text
        self.lemma = lemma
        self.pos = pos
        self.tag = tag
        self.head = head
        self.dep = dep
        self.children = children


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.data = self.load_parse_result()
        self.converted_sentence = self.convert_sentence()

    def load_parse_result(self):
        nlp = spacy.load("en_core_web_sm")
        data = nlp(self.sentence)
        return data

    def convert_sentence(self):
        """
        Converts sentence to Word objects.
        :return: converted sentence
        """
        word_array = []
        for token in self.data:
            word_array.append(Word(token.text, token.lemma_, token.pos_,
                                   token.tag_, token.head, token.dep_,
                                   [child for child in token.children]))
        return word_array

    def get_converted_sentence(self):
        return self.converted_sentence

    def get_root(self):
        for word in self.converted_sentence:
            if word.dep == "ROOT":
                return word.text
        return None

    # noinspection PyTypeChecker
    def get_triples(self):
        triples = [None] * 3

        for index in range(len(self.converted_sentence)):
            # very rudimentary solution for a non-greedy search
            # will probably have to optimize later
            found_all = True
            for phrase in triples:
                if phrase is None:
                    found_all = False

            if found_all:
                break

            word = self.converted_sentence[index]
            if word.dep == "ROOT":
                triples[1] = word.text
            elif word.dep == "nsubj":
                span = self.data[self.data[index].left_edge.i:self.data[index].right_edge.i + 1]
                triples[0] = str(span)
            elif word.dep == "dobj":
                span = self.data[self.data[index].left_edge.i:self.data[index].right_edge.i + 1]
                triples[2] = str(span)

        return triples


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
    print("Original sentence:", tokenized_article[1], "\n")

    # This sentence is now represented as a list of Word objects
    sentence_obj = Sentence(tokenized_article[1])
    converted_sentence = sentence_obj.get_converted_sentence()

    for object in converted_sentence:
        # problem 40: text, lemma, pos
        # problem 41: head, dep, children
        print(object.text, object.lemma, object.pos, object.tag,
              object.head, object.dep, object.children)

    """
    42. Show root words
    For each sentence, extract the root word (whose head is ROOT).
    """
    root = sentence_obj.get_root()
    print("\nRoot:", root, "\n")

    """
    45. Triple with subject, verb, and direct object
    Extract tuples from dependency trees where:
        - subject is a nominal subject of a verb in the past tense
        - predicate is the verb in the past tense
        - object is a direct object of the verb
        
    46. Expanding subjects and objects
    """
    print("Triples:", Sentence(tokenized_article[1]).get_triples())
