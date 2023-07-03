#!/usr/bin/python3

"""
This script takes a URL and email address as command line arguments,
sends a POST request to the URL with the email address
as the body of the request, and displays the response body in UTF-8 encoding.
"""

# Import necessary libraries
from sys import argv
import requests

if __name__ == "__main__":
    # Retrieve the URL and email address from command line arguments
    url = argv[1]
    email = argv[2]

    # Create a dictionary with the email address as the value for the key
    payload = {'email': email}

    # Send a POST request to the specified URL with the payload data
    # in the request body
    response = requests.post(url, data=payload)

    # Print the response body in UTF-8 encoding
    print(response.text)
