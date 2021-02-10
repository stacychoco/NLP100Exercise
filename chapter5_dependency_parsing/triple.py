# Triple Extraction Demo
# Note: need to install Java in order for this to work
# Source: https://github.com/philipperemy/Stanford-OpenIE-Python

from openie import StanfordOpenIE


def extract_triples(text):
    with StanfordOpenIE() as client:
        triples = [triple for triple in client.annotate(text)]
    return triples


if __name__ == '__main__':
    with open("dev.spellchecked.src", 'r') as file:
        jfleg = file.read()
    triples = extract_triples(jfleg)
    for object in triples:
        print(object)
