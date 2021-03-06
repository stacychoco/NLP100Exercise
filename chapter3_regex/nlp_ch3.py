"""
nlp_ch3.py

NLP 100 Exercise

Chapter 3: Regular Expression

Author: Stacy Nguyen
"""

from collections import OrderedDict
import os
import json
import re
import requests


def read_json(json_file):
    """
    This function will read from a file which has several json objects in it
    and put them into a list of dictionaries (json objects)

    :param json_file: a string name of the file we're reading from
    :return json_list: list of json objects
    """
    # note to self: this can be done in pandas within a line :)
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
    Creates a file and writes a body article to it.
    :param file_name: name of the file to be written to
    :param body: body of the article
    """
    if not os.path.exists(file_name) or file_is_empty(file_name):
        with open(file_name, 'rw') as file:
            file.write(body)


def file_is_empty(file_name):
    # checks if a file is empty
    return os.stat(file_name).st_size == 0


def extract_category_lines(file_name):
    """
    Extracts the category lines from a given article (text file)
    :param file_name: name of the text file
    :return: list of category lines
    """
    category_lines = []
    with open(file_name, 'r') as file:
        for line in file:
            if re.search(r"^\[\[Category:.*]]", line):
                category_lines.append(line)
    return category_lines


def extract_category_names(category_lines):
    """
    Extracts the category names from a list of category lines
    :param category_lines: list of category lines
    :return: list of category names
    """
    category_names = []
    for line in category_lines:
        search = re.search(r":([\w -]+)", line)
        if search:
            category_names.append(search.group(1))
    return category_names


def extract_sections(file_name):
    """
    Extracts section names in the article with their levels.
    :param file_name: name of the article
    :return: dictionary (key: section name, value: level)
    """
    # ordered dict will preserve the order of the section names
    section_dict = OrderedDict()
    with open(file_name, 'r') as file:
        for line in file:
            search = re.search(r"^(={2,6})(.+)\1", line)
            if search:
                section_dict[search.group(2)] = len(search.group(1)) - 1
    return section_dict


def extract_media_references(article):
    """
    Extracts references to media files linked from the article
    :param article: name of the article (string)
    :return: list of links
    """
    media_list = []
    with open(article, 'r') as file:
        for line in file:
            # quick and dirty but gets the job done. surely there is a better way to approach this?
            search = re.search(r'<ref[^>]*>[^<]*url=([^ |]+)[ |]+[^<]*</ref>', line)
            if search:
                media_list.append(search.group(1))
    return media_list


def get_infobox(article):
    """
    Gets the infobox from the given article.
    I realized there are better ways to do this but this is an excuse for me to practice regex haha...
    :param article: name of article
    :return: string of the infobox
    """
    infobox_str = ""
    found_infobox = False

    with open(article, 'r') as file:
        for line in file:
            match1 = re.match(r'{{Infobox country', line)
            match2 = re.match(r'}}', line)
            if match1:
                infobox_str += line
                found_infobox = True
            elif match2:
                infobox_str += line
                break
            elif found_infobox:
                infobox_str += line

    return infobox_str


def extract_infobox(article):
    """
    Extracts infobox into a dictionary object from an article txt file
    :param article: article to extract from
    :return: infobox dictionary
    """
    infobox_str = get_infobox(article)
    infobox_list = infobox_str.splitlines()
    infobox_dict = OrderedDict()
    latest_group = ""

    for line in infobox_list:
        search = re.search(r'^\| ([^=]*) = (.*)', line)
        if search:
            latest_group = search.group(1).strip()
            infobox_dict[search.group(1).strip()] = search.group(2)
        else:
            if latest_group:
                infobox_dict[latest_group] += line
    return infobox_dict


def remove_emphasis_markup(dict):
    for key in dict:
        replacement = re.sub("'{2,4}", "", dict[key])
        dict[key] = replacement
    return dict


def remove_internal_links(dict):
    for key in dict:
        replacement1 = re.sub(r"\[\[", "", dict[key])
        replacement2 = re.sub(r"]]", "", replacement1)
        dict[key] = replacement2
    return dict


def get_image_url(image_name):
    """
    Get URL of image using mediawiki API.
    The function below closely resembles the mediawiki example in the following link:
    https://www.mediawiki.org/wiki/API:Imageinfo
    :param image_name: name of image file
    :return: url of image
    """
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:" + image_name,
        "iiprop": "url"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    image_url = ""

    for key in PAGES:
        image_url = PAGES[key]["imageinfo"][0]["url"]

    return image_url


if __name__ == '__main__':
    """
    20. Read JSON documents
    Read the JSON documents and output the body of the article about the United Kingdom. 
    Reuse the output in problems 21-29.
    """
    # read the json file into a list of json objects
    json_data = read_json('enwiki-country.json')
    # extract the UK paragraph and write it to a text file
    uk_body = read_body("United Kingdom", json_data)
    write_to_file("uk_article.txt", uk_body)

    """
    21. Lines with category names
    Extract lines that define the categories of the article.
    """
    cat_lines = extract_category_lines("uk_article.txt")

    """
    22. Category names
    Extract the category names of the article.
    """
    cat_names = extract_category_names(cat_lines)
    # for name in cat_names:
    #     print(name)
    # print(len(cat_names))

    """
    23. Section structure
    Extract section names in the article with their levels. 
    For example, the level of the section is 1 for the MediaWiki markup 
    "== Section name ==".
    """
    section_names = extract_sections("uk_article.txt")
    # print(f'There are {len(section_names)} sections in total.\n')
    # for name in section_names:
    #     print(f'{name}: Level {section_names[name]}')

    """
    24. Media references
    Extract references to media files linked from the article.
    """
    media_refs = extract_media_references("uk_article.txt")
    # for ref in media_refs:
    #     print(ref)
    # print(len(media_refs))

    """
    25. Infobox
    Extract field names and their values in the Infobox “country”, 
    and store them in a dictionary object.
    
    26. Remove emphasis markups
    In addition to the process of the problem 25, 
    remove emphasis MediaWiki markups from the values.
    
    27. Remove internal links
    In addition to the process of the problem 26, 
    remove internal links from the values. See Help:Cheatsheet.
    """
    # problem 25
    infobox_fields = extract_infobox("uk_article.txt")
    # problem 26
    infobox_without_markups = remove_emphasis_markup(infobox_fields)
    # problem 27
    infobox_without_links = remove_internal_links(infobox_without_markups)
    # print(f'There are {len(infobox_without_links)} infobox fields in total.\n')
    # for field in infobox_without_links:
    #     print(f'{field}: {infobox_without_links[field]}')

    """
    29. Country flag
    Obtain the URL of the country flag by using the analysis result of Infobox. 
    (Hint: convert a file reference to a URL by calling imageinfo in MediaWiki API)
    """
    flag_url = get_image_url(infobox_without_links['image_flag'])
    # print(flag_url)
