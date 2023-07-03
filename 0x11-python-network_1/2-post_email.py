#!/usr/bin/python3

"""
This script takes a URL and email address as command line arguments,
sends a POST request to the URL with the email address as the body
of the request, and displays the response body in UTF-8 encoding.
"""

# Import necessary libraries
from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Retrieve the URL and email address from command line arguments
    url = argv[1]
    email = argv[2]

    # Encode the email address as a dictionary with a single key-value pair
    data_dict = {'email': email}

    # Encode the dictionary as a URL-encoded string, then encode it as ASCII
    encoded_data = urllib.parse.urlencode(data_dict).encode('ascii')

    # Create a request object with the URL and encoded data as parameters
    url_request = urllib.request.Request(url, encoded_data)

    # Send the request and store the response in a variable
    with urllib.request.urlopen(url_request) as response:
        # Decode and print the response body in UTF-8 encoding
        print(response.read().decode('utf-8'))
