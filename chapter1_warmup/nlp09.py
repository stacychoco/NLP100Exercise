"""
NLP 100 Exercise

09. Typoglycemia

Write a program with the specification:
    Receive a word sequence separated by space
    For each word in the sequence:
        If the word is no longer than four letters, keep the word unchanged
        Otherwise,
            Keep the first and last letters unchanged
            Shuffle other letters in other positions (in the middle of the word)
Observe the result by giving a sentence,
e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.

Author: Stacy Nguyen
"""

import random


def typoglycemia(sentence):
    word_list = sentence.split()
    new_list = []
    for word in word_list:
        if len(word) > 4:
            to_shuffle = list(word[1:-1])
            random.shuffle(to_shuffle)

            new_word = ''.join(to_shuffle)
            new_word = word[0] + new_word + word[-1]
            new_list.append(new_word)
        else:
            new_list.append(word)

    return new_list


if __name__ == '__main__':
    print(typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"))
