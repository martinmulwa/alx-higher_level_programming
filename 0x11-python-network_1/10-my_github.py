#!/usr/bin/python3

"""
Retrieve user ID from GitHub API using HTTP Basic authentication
"""

# Import necessary libraries
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Define the URL for the GitHub API endpoint
    url = 'https://api.github.com/user'

    # Send a GET request to the GitHub API with HTTP Basic authentication
    response = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))

    # Extract and print the user ID from the API response
    print(response.json().get('id'))
