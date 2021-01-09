"""
NLP 100 Exercise

02. “shoe” + “cold” = “schooled”
Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.

Author: Stacy Nguyen
"""


def concatenate_two_strings(s1, s2):
    """
    This function concatenates each character of string 1 and 2 one by one to get a new string.
    :param s1: string 1
    :param s2: string 2
    :return new_str: concatenated string
    """
    new_str = ""
    for x, y in zip(s1, s2):
        new_str += x + y

    return new_str


if __name__ == '__main__':
    print(concatenate_two_strings("shoe", "cold"))
