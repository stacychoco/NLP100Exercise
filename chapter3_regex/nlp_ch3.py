"""
nlp_ch3.py

NLP 100 Exercise

Chapter 3: Regular Expression

Author: Stacy Nguyen
"""

from os import path
import json


def read_json(json_file):
    """
    This function will read from a file which has several json objects in it
    and put them into a list of dictionaries (json objects)

    :param json_file: a string name of the file we're reading from
    :return json_list: list of json objects
    """
    json_list = []
    with open(json_file, 'r') as file:
        for json_object in file:
            json_dict = json.loads(json_object)
            json_list.append(json_dict)

    return json_list


def read_body(title, list):
    """
    Reads the body of the article from the given list of json objects.
    :param title: title of the article
    :param list: list of json objects
    :return: body paragraph if possible, otherwise None
    """
    for dict in list:
        if dict["title"] == title:
            return dict["text"]
    return None


def write_to_file(file_name, body):
    """
    Creates a fiie and writes a body article to it.
    :param file_name: name of the file to be written to
    :param body: body of the article
    """
    if not path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write(body)


if __name__ == '__main__':
    """
    20. Read JSON documents
    Read the JSON documents and output the body of the article about the United Kingdom. 
    Reuse the output in problems 21-29.
    """
    json = read_json('enwiki-country.json')
    uk_body = read_body("United Kingdom", json)
    write_to_file("uk_article.txt", uk_body)
