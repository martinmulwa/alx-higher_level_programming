#!/usr/bin/python3

"""
This script takes a URL as a command line argument,
sends a GET request to the URL, and displays the response body
in UTF-8 encoding. If an HTTP error occurs, it prints the error code.
"""

# Import necessary libraries
from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        # Send a GET request to the URL and store the response in a variable
        with urllib.request.urlopen(argv[1]) as response:
            # If the request succeeds, decode and print the response body
            # in UTF-8 encoding
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print("Error code: {}".format(e.code))
