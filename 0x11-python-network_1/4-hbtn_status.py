#!/usr/bin/python3

"""
This script sends a GET request to https://alx-intranet.hbtn.io/status
and displays the response body.
"""

# Import necessary libraries
import requests

if __name__ == "__main__":
    # Send a GET request to the specified URL
    response = requests.get('https://alx-intranet.hbtn.io/status')

    # Print the type and content of the response body
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
