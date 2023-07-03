#!/usr/bin/python3

"""
Searches for user by letter, POST request to server, display result or error
"""

# Import necessary libraries
from sys import argv
import requests

if __name__ == "__main__":
    # Check if a letter argument was provided, set to empty string if not
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]

    # Define the URL and payload data for the request
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    # Send a POST request with the payload data to the server
    response = requests.post(url, data=payload)

    try:
        # Attempt to parse the response body as JSON
        json_data = response.json()

        # Check if the response contains any data
        if json_data:
            # If data is found, print the user ID and name
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            # If no data is found, print a message that no results were found
            print("No result")
    except ValueError as e:
        # If the response body is not valid JSON, print an error message
        print("Not a valid JSON")
