#!/usr/bin/python3
"""8-class_to_json Module
"""
import json


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object

    Args:
        obj: an instance of a Class
    """
    return json.dumps(obj, default=vars)
