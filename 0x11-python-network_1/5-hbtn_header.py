#!/usr/bin/python3

"""
This script takes a URL as a command line argument,
sends a GET request to the URL,
and displays the value of the 'X-Request-Id' header in the server's response.
"""

# Import necessary libraries
from sys import argv
import requests

if __name__ == "__main__":
    # Send a GET request to the URL specified in the command line argument
    # and store the response in a variable
    response = requests.get(argv[1])

    # Print the value of 'X-Request-Id' header in the response
    print(response.headers.get('X-Request-Id'))
