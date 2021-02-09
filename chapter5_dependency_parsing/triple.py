# Triple Extraction Demo
# Note: need to install Java in order for this to work
# Source: https://github.com/philipperemy/Stanford-OpenIE-Python

from openie import StanfordOpenIE


def extract_triples(text):
    with StanfordOpenIE() as client:
        triples = [triple for triple in client.annotate(text)]
    return triples


if __name__ == '__main__':
    text = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving".'
    triples = extract_triples(text)
    print()
    for obj in triples:
        values = [value for value in obj.values()]
        print(values)
