#!/usr/bin/python3
""" 5-text_indentation.py """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        test: string to be printed

    Returns: None
    """
    # check that text is a string
    if type(text) != str:
        raise TypeError("text must be a string")

    flag = False  # you have found a printable character
    for c in text:
        if c == " " and not flag:
            continue

        flag = True
        print(c, end="")

        if c in ['.', ':', '?']:
            print("\n")
            flag = False
