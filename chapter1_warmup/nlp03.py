"""
NLP 100 Exercise

03. Pi
Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”.
into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.

Author: Stacy Nguyen
"""

from collections import OrderedDict
from string import ascii_lowercase


def number_of_words(sentence):
    """
    Returns a dictionary with the key being a word and the value being the number of letters in that word.

    :param sentence: the sentence which will be split into a list of words to put into the dictionary
    :return: dictionary
    """

    # split sentence by space
    word_list = sentence.split()
    # ordered dict will preserve the order of the words
    word_dict = OrderedDict()

    for word in word_list:
        # creating new_word string to only count alphabetical letters
        new_word = ""
        for char in word:
            if char.lower() in ascii_lowercase:
                new_word += char

        word_dict[new_word] = len(new_word)

    return word_dict


if __name__ == '__main__':
    print(number_of_words("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
