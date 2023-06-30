#!/bin/bash
# This script sends a POST request to the specified URL with custom variables, and displays the response body
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -s "$1"
