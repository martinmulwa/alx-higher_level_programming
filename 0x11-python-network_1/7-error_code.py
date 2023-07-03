#!/usr/bin/python3

"""
GET request, print response or error code
"""

# Import necessary libraries
from sys import argv
import requests

if __name__ == "__main__":
    # Send a GET request to the URL
    response = requests.get(argv[1])

    # Check if an HTTP error occurred
    if response.status_code >= 400:
        # If an error occurred, print the error code
        print("Error code: {}".format(response.status_code))
    else:
        # If the request succeeded, print the response body
        print(response.text)
