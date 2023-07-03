#!/usr/bin/python3

"""
This script takes a URL as a command line argument, fetches the URL,
and displays the value of the 'X-Request-Id' header in the server's response.
"""

# Import necessary libraries
from sys import argv
import urllib.request

if __name__ == "__main__":
    # Create a request object for the given URL
    url_request = urllib.request.Request(url=argv[1])

    # Send the request and store the response in a variable
    with urllib.request.urlopen(url_request) as response:
        # Print the value of 'X-Request-Id' header in the response
        print(response.getheader('X-Request-Id'))
