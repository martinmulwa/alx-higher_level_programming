#!/usr/bin/python3

"""
Retrieve the last 10 commits for a GitHub repository using the GitHub API
"""

# Import necessary libraries
from sys import argv
import requests

if __name__ == "__main__":
    # Define the URL for the GitHub API endpoint
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Parse the response body as JSON and extract the list of commits
    commits = response.json()

    # Print the SHA and author name for the last 10 commits
    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
