"""
NLP 100 Exercise

08. cipher text
Implement a function cipher that converts a given string with the specification:

Every alphabetical lowercase letter c is converted to a letter whose ASCII code is
(219 - [the ASCII code of c])

Keep other letters unchanged.
Use this function to cipher and decipher an English message.

Author: Stacy Nguyen
"""

from string import ascii_lowercase


def cipher(text):
    new_text = ""
    for char in text:
        if char in ascii_lowercase:
            # ord(char) gets ascii code of char
            code = 219 - ord(char)
            # chr(code) gets the character encoded by the ascii number
            new_text += chr(code)
        else:
            new_text += char
    return new_text


if __name__ == '__main__':
    # expected result: r wlm'g pmld dszg gl hzb
    print(cipher("i don't know what to say"))
    # expected result: i don't know what to say
    print(cipher("r wlm'g pmld dszg gl hzb"))
