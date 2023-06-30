#!/bin/bash
# This script sends a JSON POST request with the contents of a file in the body, and displays the response body
curl -X POST -H "Content-Type: application/json" -d "@$2" -s "$1"
