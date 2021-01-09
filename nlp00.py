"""
NLP 100 Exercise

00. Reversed string
Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).

Author: Stacy Nguyen
"""


def reverse_string(s):
    # S [ start : stop : step ] returns the portion of the string from index start to index stop, at a step size step.
    return s[::-1]


if __name__ == '__main__':
    print(reverse_string("stressed"))
