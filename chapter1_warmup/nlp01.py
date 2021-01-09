"""
NLP 100 Exercise

01. “schooled”
Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.

Author: Stacy Nguyen
"""


def concatenate_odd_characters(s):
    new_str = ""
    for i in range(1, len(s), 2):
        new_str += s[i]

    return new_str


if __name__ == '__main__':
    print(concatenate_odd_characters("schooled"))
