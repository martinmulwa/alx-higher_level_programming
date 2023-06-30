#!/bin/bash
# This script sends a GET request to the specified URL with a custom header variable, and displays the response body
curl -H "X-School-User-Id: 98" -s "$1"
